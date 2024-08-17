from pymongo import MongoClient

# Create the MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['softwareServicesDB']
collection = db['ODINSS']

# Function to get the next ID
def serviceID():
    last_service = collection.find_one(sort=[("ID", -1)])
    if last_service and 'ID' in last_service:
        return last_service['ID'] + 1
    else:
        return 1

# Function to create a software service
def createService():
    service_name = input("\nEnter a Software Service name: ")
    new_id = serviceID()
    service = {
        'ID': new_id,
        'Software Service': service_name,
        '2 Year Support': bool(input("Is 2 Year Support available? (True/False): ")),
        'Estimated Hours of Work': float(input("Enter the Estimated Hours of Work: ")),
        'Cost': float(input("Enter the Cost: "))
    }
    collection.insert_one(service)
    print(f"\nService created with ID: {new_id}")
    print(f"You have added: {service_name} to the database")

# Function to read and display all available software services
def readServices():
    services = collection.find({}, {"_id": 0, "ID": 1, "Software Service": 1, "2 Year Support": 1, "Estimated Hours of Work": 1, "Cost": 1})
    for service in services:
        print(service)

# Function to update a software service
def updateService():
    service_id = int(input("\nEnter the ID of the service to update: "))
    field_to_update = input("Enter the field to update: (S)Software Service, (Y)2 Year Support, (E)Estimated Hours of Work, (C)Cost: ")
    new_value = input(f"Enter the new value for {field_to_update}: ")

    if field_to_update in ['E', 'e', 'C', 'e']:
        new_value = float(new_value)
    elif field_to_update in ['Y', 'y']:
        new_value = bool(new_value)
    elif field_to_update in ['S', 's']:
        new_value = str(new_value)

    result = collection.update_one({'ID': service_id}, {'$set': {field_to_update: new_value}})
    if result.modified_count > 0:
        print("Service updated successfully.")
    else:
        print("No service found with the provided ID.")

# Function to delete a software service
def deleteService():
    service_id = int(input("\nEnter the ID of the service to delete: "))
    result = collection.delete_one({'ID': service_id})
    if result.deleted_count > 0:
        print("Service deleted successfully.")
    else:
        print("No service found with the provided ID.")

# Main
def main():
    while True:
        print("\nOptions:")
        print("C. Create Software Service")
        print("R. Read (Display) Software Services")
        print("U. Update Software Service")
        print("D. Delete Software Service")
        print("E. Exit")
        
        choice = input("\nEnter your CRUDE option: ")

        if choice in ['C', 'c']:
            createService()
        elif choice in ['R', 'r']:
            readServices()
        elif choice in ['U', 'u']:
            updateService()
        elif choice in ['D', 'd']:
            deleteService()
        elif choice in ['E', 'e']:
            print("Exiting...")
            break
        else:
            print("That is not an option, please try again.")

if __name__ == "__main__":
    main()
