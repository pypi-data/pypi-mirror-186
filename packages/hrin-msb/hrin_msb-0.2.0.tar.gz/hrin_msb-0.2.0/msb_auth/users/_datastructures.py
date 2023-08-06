from dataclasses import dataclass


@dataclass
class UserName:
	first: str
	middle: str
	last: str
	full: str


@dataclass
class UserRole:
	id: int
	name: str


@dataclass
class UserCountry:
	id: int
	name: str


@dataclass
class UserAccountType:
	id: int
	name: str


@dataclass
class UserPermissions:
	pass


@dataclass
class UserImage:
	url: str
	id: int


@dataclass
class UserRegisteredApp:
	id: int
	name: str


@dataclass
class UserLocation:
	id: int
	name: str
