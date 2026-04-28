from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   
    return render(request,'patients/home.html')

def about(request):
    peoples = [
        {"id": 1, "name": "Sok Dara", "age": 25, "city": "Phnom Penh", "job": "Teacher", "salary": 450},
        {"id": 2, "name": "Chantha Vann", "age": 30, "city": "Siem Reap", "job": "Tour Guide", "salary": 500},
        {"id": 3, "name": "Srey Neang", "age": 28, "city": "Battambang", "job": "Nurse", "salary": 600},
        {"id": 4, "name": "Vuthy Heng", "age": 35, "city": "Kampot", "job": "Farmer", "salary": 300},
        {"id": 5, "name": "Davy Kim", "age": 22, "city": "Sihanoukville", "job": "Student", "salary": 150},
        {"id": 6, "name": "Rithy Chea", "age": 40, "city": "Phnom Penh", "job": "Manager", "salary": 900},
        {"id": 7, "name": "Sokha Ly", "age": 27, "city": "Takeo", "job": "Teacher", "salary": 420},
        {"id": 8, "name": "Pisey Nhem", "age": 33, "city": "Kandal", "job": "Driver", "salary": 350},
        {"id": 9, "name": "Sophea Oun", "age": 29, "city": "Kep", "job": "Seller", "salary": 280},
        {"id": 10, "name": "Makara Chhun", "age": 31, "city": "Pursat", "job": "Farmer", "salary": 320},
        {"id": 11, "name": "Bopha Meas", "age": 26, "city": "Prey Veng", "job": "Accountant", "salary": 550},
        {"id": 12, "name": "Sokun Thorn", "age": 34, "city": "Koh Kong", "job": "Fisherman", "salary": 300},
        {"id": 13, "name": "Mony Roth", "age": 24, "city": "Kratie", "job": "Photographer", "salary": 400},
        {"id": 14, "name": "Visal Lim", "age": 38, "city": "Stung Treng", "job": "Police", "salary": 500},
        {"id": 15, "name": "Srey Mom", "age": 21, "city": "Ratanakiri", "job": "Student", "salary": 150},
        {"id": 16, "name": "Chan Sophal", "age": 45, "city": "Mondulkiri", "job": "Tour Guide", "salary": 520},
        {"id": 17, "name": "Dara Keo", "age": 32, "city": "Svay Rieng", "job": "Mechanic", "salary": 450},
        {"id": 18, "name": "Kanika Phan", "age": 28, "city": "Oddar Meanchey", "job": "Teacher", "salary": 430},
        {"id": 19, "name": "Rady Sok", "age": 36, "city": "Banteay Meanchey", "job": "Security", "salary": 350},
        {"id": 20, "name": "Chenda Vong", "age": 23, "city": "Kampong Cham", "job": "Seller", "salary": 300}
        ]
    
    return render(request,'patients/about.html',{"peoples":peoples})

def  register(request):
   return render(request,'patients/register.html')