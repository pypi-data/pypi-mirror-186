from dataclasses import dataclass


@dataclass
class Config:
    max_users: int
    use_email: bool
    use_sms: bool
