import os
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

import yaml

# data model

DIR, _ = os.path.split(os.path.abspath(__file__))
with open(os.path.join(DIR, 'enum_translation.yml')) as f:
    trans_data = yaml.safe_load(f)

class Location(BaseModel):
    lat: float
    lon: float

class Rating(BaseModel):
    avg_rating: float
    avg_on_time: float
    avg_service: float
    avg_accurate_profile_description: float


class BaseProfile(BaseModel):
    wallet: Optional[str]
    uid: Optional[str]
    name: str
    referrer: str = None
    gender: str = None
    register_timestamp: int = 0


class MultiLangEnum(str, Enum):
    @classmethod
    def translates(cls):
        return trans_data[cls.__name__]

class Gender(MultiLangEnum):
    male = 'male'
    female = 'female'

class EyeColor(MultiLangEnum):
    blue = 'blue'
    black = 'black'
    brown = 'brown'
    green = 'green'
    other = 'other'

class HairColor(MultiLangEnum):
    blue = 'blue'
    black = 'black'
    blond = 'blond'
    red = 'red'
    other = 'other'

class Ethnicity(MultiLangEnum):
    asian = 'asian'
    australian = 'australian'
    caucasian = 'caucasian'

class Build(MultiLangEnum):
    athletic = 'athletic'
    chunky = 'chunky'
    fit = 'fit'
    slender = 'slender'
    skinny = 'skinny'


class Bust(MultiLangEnum):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g_plus = 'g_plus'


class DressSize(MultiLangEnum):
    small_minus = 'small_minus'
    small = 'small'
    medium = 'medium'
    large = 'large'
    large_plus = 'large_plus'

class SpeakingLanguage (MultiLangEnum):
    english = 'english'
    mandarin = 'mandarin'
    japanese = 'japanese'
    korean = 'korean'
    cantonese = 'cantonese'

class PaymentMethod (MultiLangEnum):
    usdt = 'usdt'

class TimeSlotStatus(MultiLangEnum):
    available = 'available'
    attempt = 'attempt'
    pending_payment = 'pending_payment'
    booked = 'booked'
    locked = 'locked'


class BookingStatus(MultiLangEnum):
    attempt = 'attempt'
    pending_payment = 'pending_payment'
    archived = 'archived'
    confirmed = 'confirmed'
    cancel_attempt = 'cancel_attempt'
    canceled = 'canceled'
    fulfilled = 'fulfilled'
    deleted = 'deleted'  # need this? or simply delete it. as _id will conflict


class ProviderProfile(BaseProfile):
    address: str
    postcode: Optional[int]
    city: Optional[str]
    country: Optional[str]
    age: int = 27
    location: Location
    contact_detail: str = None
    rate_aud: int = 150
    hair_color: Optional[HairColor]
    build: Optional[Build]
    ethnicity: Optional[Ethnicity]
    eye_color: Optional[EyeColor]
    bio: Optional[str]
    photos: List[str] = []
    height: Optional[int]
    bust: Optional[Bust]
    avg_on_time: Optional[float]
    avg_service: Optional[float]
    avg_rating: Optional[float]
    avg_accurate_profile_description: Optional[float]
    dress_size: Optional[DressSize]
    speaking_language: List[SpeakingLanguage] = []
    payment: List[PaymentMethod] = []
    instruction_images: Optional[List[str]] = []
    instruction_text: Optional[str]


class ConsumerProfile(BaseProfile):
    pass


class TimeSlot(ProviderProfile):
    slot_id: int  # the slot id, YYYYmmddXX
    slot_status: TimeSlotStatus = TimeSlotStatus.available


# details of a booking, which is shown to the provider and consumer
class BookingDetail(TimeSlot):
    total_fee_aud: int


class BookingHistory(BaseModel):  # state chagen history of a booking
    ationer: str
    timestamp: int
    additional_comment: Optional[str]


class Booking(BaseModel):  # booking to a timeslot
    consumer_uid: str
    provider_uid: str
    all_slots: List[int] = []
    status: BookingStatus
    consumer_comments: Optional[str]
    consumer_rating: Optional[float]
    provider_comments: Optional[str]
    provider_rating: Optional[float]
    last_update: int
    detail: BookingDetail
    total_fee_aud: int
    book_time: int  # epoch second of booked
    history: List[BookingHistory] = []


class Transaction(BaseModel):
    consumer_uid: str
    provider_uid: str
    booking: Booking
    timestamp: int
    total_fee_aud: int


# response model


class SingleProviderResponse(ProviderProfile):
    pass


class SingleConsumerResponse(ConsumerProfile):
    pass


class SingleTimeSlotResponse(TimeSlot):
    pass


class SingleBookingResponse(Booking):
    pass


class SingleTransactionResponse(Transaction):
    pass


class ProviderListResponse(BaseProfile):
    results: List[ProviderProfile] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]


class TimeSlotListResponse(BaseProfile):
    results: List[TimeSlot] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]


class BookingListResponse(BaseProfile):
    results: List[Booking] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]


class OrderListResponse(BaseProfile):
    results: List[Booking] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]

# general model


class HealthResponse(BaseModel):
    status: str

class NotificationsModel(BaseModel):
    notifications: List[str] = []