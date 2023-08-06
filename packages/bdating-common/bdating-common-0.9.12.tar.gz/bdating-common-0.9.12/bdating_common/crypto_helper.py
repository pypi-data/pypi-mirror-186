"""
Crypto helper.

"""
import logging
from tokenize import Number
import web3
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
# from web3.auto.infura.mainnet import w3
from web3.exceptions import TransactionNotFound
import pickle
import sys
from enum import Enum
import json
import requests

logger = logging.getLogger(__name__)

class TxnStatusEnum(Enum):
  TXN_MISMATCHED = -2
  TXN_REVERTED = -1
  TXN_NOT_READY = 0
  TXN_CONFIRMED = 1


networks = {
  'bnb_test': {
    # 'rpc_url': 'https://data-seed-prebsc-1-s1.binance.org:8545/',
    # 'chain_id': '97',
    # 'currency': 'BNB',
    # 'explorer_url': 'https://testnet.bscscan.com',
    'w3_client': Web3(HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545/')),
    'minimal_confirm': 2
  },
  'bnb_main': {
    # 'rpc_url': 'https://bsc-dataseed1.ninicoin.io',
    # 'chain_id': '56',
    # 'currency': 'BNB',
    # 'explorer_url': 'https://bscscan.com',
    'w3_client': Web3(HTTPProvider('https://bsc-dataseed1.ninicoin.io')),
    'minimal_confirm': 3
  },
  'eth_main': {
    # 'rpc_url': 'https://rpc.ankr.com/eth',  # https://rpc.info/
    # 'chain_id': '1',
    # 'currency': 'ETH',
    'explorer_url': 'https://rpc.ankr.com/eth',
    'w3_client': Web3(HTTPProvider('https://rpc.ankr.com/eth')),
    'minimal_confirm': 3
  },
  'eth_goerli': {
    'rpc_url': 'https://rpc.ankr.com/eth_goerli',
    'chain_id': '5',
    'currency': 'ETH',
    'explorer_url': 'https://goerli.etherscan.io',
    'w3_client': Web3(HTTPProvider('https://rpc.ankr.com/eth_goerli')),
    'minimal_confirm': 3,
    'contract_address': '0xB99d86242bb33F874F1Eb59dd0C403369a7D1D7c'
  }
}
for k, v in networks.items():
    if k.endswith(''):
        v['w3_client'].middleware_onion.inject(geth_poa_middleware, layer=0)

""" Depricated
def check_transactions_by_wallet(blockchain_address: str, network: str = 'bnb_main', Logger: object=None):
    # NOTE: WIP code. We are not sure when and how to use this method.
    w3 = networks[network]['w3_client']

    # request the latest block number
    ending_blocknumber = w3.eth.blockNumber

    # latest block number minus 100 blocks
    starting_blocknumber = ending_blocknumber - 1

    # create an empty dictionary we will add transaction data to
    tx_dictionary = {}

    print(
        f"Started filtering through block number {starting_blocknumber} to {ending_blocknumber} for transactions involving the address - {blockchain_address}...")
    for x in range(starting_blocknumber, ending_blocknumber):
        block = w3.eth.getBlock(x, True)
        for transaction in block.transactions:
            # print(transaction)
            if str(transaction['to'].lower()) == blockchain_address or str(transaction['from'].lower()) == blockchain_address:
                print(transaction)
                with open("transactions.pkl", "wb") as f:
                    hashStr = transaction['hash'].hex()
                    tx_dictionary[hashStr] = transaction
                    pickle.dump(tx_dictionary, f)
                f.close()
    print(f"Finished searching blocks {starting_blocknumber} through {ending_blocknumber} and found {len(tx_dictionary)} transactions")
"""

def check_transaction_status(transaction_hash: str, to_address: str, value: Number, chain_id: str = None, network: str = 'bnb_main') -> TxnStatusEnum:
    if chain_id is not None:
      for name, network_config in networks.items():
        if network_config.get('chain_id') == chain_id:
          network = name
    w3 = networks[network]['w3_client']
    print(f"check_transaction_status(), trying to check the following transaction on network {network}")
    print(f"check_transaction_status(), transaction hash: {transaction_hash}")
    print(f"check_transaction_status(), expected: token_contract={networks[network]['contract_address']}")
    print(f"check_transaction_status(), expected: token_to={to_address}")
    print(f"check_transaction_status(), expected: tokens_value={value}")

    minimal_confirm = networks[network]['minimal_confirm']
    try:
        txn_status = w3.eth.get_transaction_receipt(transaction_hash)['status']
        if txn_status == 0:
          logger.warning(f"Transaction {transaction_hash} was reverted by EVM!")
          return TxnStatusEnum.TXN_REVERTED

        transaction = w3.eth.get_transaction(transaction_hash=transaction_hash)

        last_block = w3.eth.get_block_number()
        print(f"Received Tranasction, {transaction}, last_block: {last_block}")
        # print(f"transaction.input= {w3.toBytes(transaction.input)}")
        # abi_endpoint = f'https://api-goerli.etherscan.io/api?module=contract&action=getabi&address=0xB99d86242bb33F874F1Eb59dd0C403369a7D1D7c'
        # abi = json.loads(requests.get(abi_endpoint).text)
        abi = "[{\"constant\":true,\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"spender\",\"type\":\"address\"},{\"name\":\"tokens\",\"type\":\"uint256\"}],\"name\":\"approve\",\"outputs\":[{\"name\":\"success\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"totalSupply\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"from\",\"type\":\"address\"},{\"name\":\"to\",\"type\":\"address\"},{\"name\":\"tokens\",\"type\":\"uint256\"}],\"name\":\"transferFrom\",\"outputs\":[{\"name\":\"success\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"decimals\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"_totalSupply\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"tokenOwner\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"name\":\"balance\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"a\",\"type\":\"uint256\"},{\"name\":\"b\",\"type\":\"uint256\"}],\"name\":\"safeSub\",\"outputs\":[{\"name\":\"c\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"pure\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"to\",\"type\":\"address\"},{\"name\":\"tokens\",\"type\":\"uint256\"}],\"name\":\"transfer\",\"outputs\":[{\"name\":\"success\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"a\",\"type\":\"uint256\"},{\"name\":\"b\",\"type\":\"uint256\"}],\"name\":\"safeDiv\",\"outputs\":[{\"name\":\"c\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"pure\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"spender\",\"type\":\"address\"},{\"name\":\"tokens\",\"type\":\"uint256\"},{\"name\":\"data\",\"type\":\"bytes\"}],\"name\":\"approveAndCall\",\"outputs\":[{\"name\":\"success\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"a\",\"type\":\"uint256\"},{\"name\":\"b\",\"type\":\"uint256\"}],\"name\":\"safeMul\",\"outputs\":[{\"name\":\"c\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"pure\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"tokenOwner\",\"type\":\"address\"},{\"name\":\"spender\",\"type\":\"address\"}],\"name\":\"allowance\",\"outputs\":[{\"name\":\"remaining\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"a\",\"type\":\"uint256\"},{\"name\":\"b\",\"type\":\"uint256\"}],\"name\":\"safeAdd\",\"outputs\":[{\"name\":\"c\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"payable\":true,\"stateMutability\":\"payable\",\"type\":\"fallback\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"name\":\"tokens\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"name\":\"tokenOwner\",\"type\":\"address\"},{\"indexed\":true,\"name\":\"spender\",\"type\":\"address\"},{\"indexed\":false,\"name\":\"tokens\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"}]" 
        if transaction['to'] != networks[network]['contract_address']:
          print(f"Transaction {transaction_hash} is not using correct contract {networks[network]['contract_address']}.")
          return TxnStatusEnum.TXN_MISMATCHED
        
        contract = w3.eth.contract(address=networks[network]['contract_address'], abi=abi)
        func_obj, func_params = contract.decode_function_input(transaction["input"])
        print(f"transaction.input.func_obj= {func_obj}")
        print(f"transaction.input.func_params= {func_params}")
        
        if last_block - transaction.get('blockNumber', sys.maxsize) >= minimal_confirm:
          if func_params.get('to').lower() == to_address.lower() and func_params.get('tokens') >= value:
            logger.info(f"Transaction {transaction_hash} is available.")
            print(f"Transaction {transaction_hash} is available.")
            return TxnStatusEnum.TXN_CONFIRMED
          else:
            logger.warning(f"Transaction {transaction_hash} has been confirmed but details mismatched!")
            logger.warning(f"Found Transaction: token_to={ func_params.get('to')} , expected: token_to={to_address} ")
            logger.warning(f"Found Transaction: tokens_value={ func_params.get('tokens')} , expected: tokens_value={value} ")
            return TxnStatusEnum.TXN_MISMATCHED
        else:
          logger.info(f"Transaction {transaction_hash} is available now but still needs more confirmation.")
          return TxnStatusEnum.TXN_NOT_READY
    except TransactionNotFound:
        logger.info(f"Transaction {transaction_hash} not found yet.")
        return TxnStatusEnum.TXN_NOT_READY

"""
did not check confidence block gap
"""
def check_transaction_status_v2(transaction_hash: str, to_address: str, value: Number, network: str = 'bnb_main') -> bool:
    w3 = networks[network]['w3_client']
    try:
      transaction = w3.eth.get_transaction(transaction_hash=transaction_hash)
      #TODO: convert bnb value from its unit
      txn_value = Web3.fromWei(transaction['value'], 'ether')
      txn_status = w3.eth.get_transaction_receipt(transaction_hash)['status']
      # status ==1 should be able to present the succeed of txn
      if txn_status == 1:
        if str(transaction['to']).lower() == to_address.lower() and txn_value >= value:
          logger.info(f"Transaction {transaction_hash} is available.")
          print(f"Transaction {transaction_hash} is available.")
          return True
        else:
          logger.warning(f"Transaction {transaction_hash} received but details mismatched. value={txn_value}, to_addr={transaction['to']}")
          return False
      else:
        logger.warning(f"Transaction {transaction_hash} not confidence yet or failed")
        return False


    except TransactionNotFound:
      logger.info(f"Transaction {transaction_hash} not found yet.")
      return False

if __name__ == '__main__':
    # print(check_transaction_status(transaction_hash='0xc878288e8222cc472a450a44ac0674498290757ac101f54b79be05c03d023d51', 
    #   to_address='0x840851d656e2575a3d524af2be7249dcdbaa718c', 
    #   value=0.000001,
    #   network='eth_goerli'))


    # w3 = Web3(HTTPProvider('https://rpc.ankr.com/eth_goerli'));
    # print(w3.eth.filter('pending'))
    # print(Web3.fromWei(677262836600000, 'ether'))

    print(check_transaction_status(transaction_hash='0x11207b48fb51c065adfdab9064c732067cd9a5514b6d33a99c2bc5dbc6163b38', 
      to_address='0x978258905A52De6afFd8F04929204215c1B59A87', 
      value=15000,
      network='eth_goerli')) 

