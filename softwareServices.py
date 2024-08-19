from pymongo import MongoClient

# Create the MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['softwareServicesDB']
collection = db['ODINSS']

# Function to get the next ID
def serviceID():
    lastService = collection.find_one(sort=[("ID", -1)])
    if lastService and 'ID' in lastService:
        return lastService['ID'] + 1
    else:
        return 1

# Function to create a software service
def createService():
    serviceName = input("\nEnter a Software Service name: ")

    supportInput = input("Is 2 year support available? ")
    if supportInput in ['true', 'yes']:
        twoYearSupport = True
    elif supportInput in ['false', 'no']:
        twoYearSupport = False
    else:
        print("Invalid, please select yes/no, or true/false")

    new_id = serviceID()
    service = {
        'ID': new_id,
        'Software Service': serviceName,
        '2 Year Support': twoYearSupport,
        'Estimated Hours of Work': float(input("Enter the Estimated Hours of Work: ")),
        'Cost': float(input("Enter the Cost: "))
    }
    collection.insert_one(service)
    print(f"\nService created with ID: {new_id}")
    print(f"You have added: {serviceName} to the database")

# Function to read and display all available software services
def readServices():
    services = collection.find({}, {"_id": 0, "ID": 1, "Software Service": 1, "2 Year Support": 1, "Estimated Hours of Work": 1, "Cost": 1})
    for service in services:
        print(service)

# Function to update a software service
def updateService():
    serviceID = int(input("\nEnter the ID of the service to update: "))
    updateField = input("Enter the field to update: (S)Software Service, (Y)2 Year Support, (E)Estimated Hours of Work, (C)Cost: ")
    
    if updateField in ['Y', 'y', '2 year support']:
        newValue = input("Is 2 Year Support available? (yes/no): ")
        if newValue.lower() in ['true', 'yes']:
            newValue = True
        elif newValue.lower() in ['false', 'no']:
            newValue = False
        else:
            print("Invalid input. Defaulting to False.")
            newValue = False
        updateField = "2 Year Support"
    else:
        newValue = input(f"Enter the new value for {updateField}: ")

        if updateField in ['E', 'e']:
            newValue = float(newValue)
            updateField = "Estimated Hours of Work"
        elif updateField in ['C', 'c']:
            newValue = float(newValue)
            updateField = "Cost"
        elif updateField in ['S', 's']:
            newValue = str(newValue)
            updateField = "Software Service"

    result = collection.update_one({'ID': serviceID}, {'$set': {updateField: newValue}})
    if result.modified_count > 0:
        print("Service updated successfully.")
        updatedService = collection.find_one({'ID': serviceID}, {"_id": 0, "ID": 1, "Software Service": 1, "2 Year Support": 1, "Estimated Hours of Work": 1, "Cost": 1})
        print("\nUpdated Service:")
        print(updatedService)
    else:
        print("No service found with the provided ID.")



# Function to delete a software service
def deleteService():
    serviceID = int(input("\nEnter the ID of the service to delete: "))
    result = collection.delete_one({'ID': serviceID})
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
