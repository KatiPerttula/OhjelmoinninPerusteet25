from datetime import datetime

reservation = {
    "user": "Mika Virtanen",   # str
    "age": 22,                    # int
    "room": "Kokoushuone A",      # str
    "start": datetime(2025, 10, 30, 14, 0),
    "end": datetime(2025, 10, 30, 16, 0),
    "confirmed": None,            # NoneType (ei vielä hyväksytty)
    "price": 25.50,               # float
    "participants": ["Satu", "Antti", "Joonas"], # list
    "time_slot": ("14:00", "16:00"),  # tuple
    "permissions": frozenset({"view"}), # frozenset
}

print(f"{reservation['user']} varasi huoneen {reservation['room']} klo {reservation['time_slot'][0]}–{reservation['time_slot'][1]}")
if reservation["confirmed"] is None:
    print("Varaus odottaa vahvistusta ⏳")