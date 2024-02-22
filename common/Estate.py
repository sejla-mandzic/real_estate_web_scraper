class Estate:
    id: int
    category: str
    price: float
    canton: str
    city: str
    state: str
    area: int
    terrace: bool
    parking: bool
    electricity: bool
    water: bool
    internet: bool
    basement: bool
    post_date: str
    build_period: str
    floor_type: str
    terrace_area: float
    cable_tv: bool
    pantry: bool
    phone_line: bool
    bathrooms_num: int
    heating_type: str

    def __init__(
        self,
        id: int,
        category: str,
        price: int,
        canton: str,
        city: str,
        state: str,
        area: float,
        terrace: bool,
        parking: bool,
        electricity: bool,
        water: bool,
        internet: bool,
        basement: bool,
        post_date: str,
        build_period: str,
        floor_type: str,
        terrace_area: float,
        cable_tv: bool,
        pantry: bool,
        phone_line: bool,
        bathrooms_num: int,
        heating_type: str,
    ):
        self.id = id
        self.category = category
        self.price = price
        self.canton = canton
        self.city = city
        self.state = state
        self.area = area
        self.terrace = terrace
        self.parking = parking
        self.electricity = electricity
        self.water = water
        self.internet = internet
        self.basement = basement
        self.post_date = post_date
        self.build_period = build_period
        self.floor_type = floor_type
        self.terrace_area = terrace_area
        self.cable_tv = cable_tv
        self.pantry = pantry
        self.phone_line = phone_line
        self.bathrooms_num = bathrooms_num
        self.heating_type = heating_type

    def to_csv_row(self) -> str:
        return f"{self.id},{self.category},{self.price},{self.canton},{self.city},{self.state},{self.area},{self.terrace},{self.parking},{self.electricity},{self.water},{self.internet},{self.basement},{self.post_date},{self.build_period},{self.floor_type},{self.terrace_area},{self.cable_tv},{self.pantry},{self.phone_line},{self.bathrooms_num},{self.heating_type}\n"
