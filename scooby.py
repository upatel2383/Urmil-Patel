# Name: Urmil Patel 
# Date: 04/14/2021 
# Program: 


#Function 
def sample1 ():
    #Open file 
    scooby_file = open ('scooby.txt', 'w')

    # Write to file 
    scooby_file.write("shaggy\n")
    scooby_file.write("scooby-doo\n")
    scooby_file.write("daphne\n")
    scooby_file.write("velma\n")

    # close file 
    scooby_file.close()

# Function 
def sample2 ():
    #open file 
    scooby_file = open ('scooby.txt', 'w')

    # write to file 
    scooby_file.write("Fred\n")
    scooby_file.write("Scrappy\n")

    # close file 
    scooby_file.close()

# main body 
sample1()
sample2()