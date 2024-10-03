import requests
import json
from faker import Faker
from webexteamssdk import WebexTeamsAPI

fake = Faker()

accessToken = "OWM5NjgxYTAtMGFkZi00NzUxLWEyMTctOTQyOTQ5OThhNTg3MDliZDBmY2UtMDFl_P0A1_1ad92174-dfe2-4740-b008-57218895946c"
#1

api = WebexTeamsAPI(access_token=accessToken)

meeting = api.meetings.create(
title="Midterm Quiz Kean",
start="2024-10-03T10:00:00Z",
end="2024-10-03T11:00:00Z",
)


print("Meeting Successfully Created!")
print("Meeting Details:", meeting)

#2

room = api.rooms.create("Kean Pogi")
api.memberships.create(room.id, personEmail="janhendrixnavales@baliuagu.edu.ph")
print("Room Successfully Created. Participant Added Succesfully.")


#3

api.messages.create(room.id, text="Dang, papajake")
print("Message Successfully Sent!")


#4

messages = api.messages.list("Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZmE4MmZjMzAtODE1Yi0xMWVmLThkMjgtODcwOThlYTJhZDA0")
for message in messages:
    print(message)


#5

def delete_message(message_id):
    api.messages.delete(message_id)
print("Message Successfully Deleted!")

delete_message('Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvZmIyMDRkYTAtODE1Yi0xMWVmLWExNjQtMDdjM2E2MmE3ZWU4')


#Part 2
#1
def generate_fake_data():
    for _ in range(10):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        print(f"Name: {fake.name()} Email: {fake.email()}, Phone: {fake.phone_number()}")

        generate_fake_data()