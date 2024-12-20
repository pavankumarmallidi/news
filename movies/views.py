from django.shortcuts import render

# Create your views here.
def movies(request):
    return render(request, 'movies.html')
def News(request,data):
    if(data=='og'):
        htmldata={
            'name':'OG',
            'information':"OG (also known as They Call Him OG) is an upcoming Indian Telugu-language gangster action thriller film written and directed by Sujeeth and produced by D. V. V. Danayya of DVV Entertainment. The film stars Pawan Kalyan, Emraan Hashmi (in his Telugu debut), and Priyanka Mohan.",
            'imsrc':'IMAGES/og.jpeg'
        }
    elif(data=='ubc'):
        htmldata={
            'name':"Ustaad  ",
            'information':'Ustaad Bhagat Singh (transl. Teacher Bhagat Singh) is an upcoming Indian Telugu-language action thriller film directed by Harish Shankar and produced by Mythri Movie Makers. The film stars Pawan Kalyan in the titular role, alongside Sreeleela, Ashutosh Rana, Nawab Shah, B. S. Avinash, Gautami and Chammak Chandra.',
            'imsrc':'IMAGES/ubs.jpeg'
        }
    elif(data=='bheemlaNayak'):
        htmldata={
            'name':"Bheemla Nayak",
            'information':'Bheemla Nayak is a 2022 Indian Telugu-language action thriller film directed by Saagar K Chandra from a screenplay by Trivikram Srinivas. The film stars Pawan Kalyan and Rana Daggubati in lead roles. It is an official remake of the 2020 Malayalam film Ayyappanum Koshiyum. The film was filmed primarily in Hyderabad between January 2021 and February 2022 although temporarily halted by the COVID-19 pandemic. It has music composed by Thaman S with cinematography by Ravi K. Chandran and editing by Naveen Nooli.',
            'imsrc':'IMAGES/bheemla.jpeg'
        }
    elif(data=='rajasaab'):
        htmldata={
            'name':"Raja Saab",
            'information':'The Raja Saab is an upcoming Indian Telugu-language romantic comedy horror film written and directed by Maruthi.[3] It is produced by People Media Factory. The film stars Prabhas in the titular role, alongside Nidhhi Agerwal, and Malavika Mohanan (in her Telugu debut) in the lead roles.',
            'imsrc':'IMAGES/rajasaab.jpeg'
        }
    elif(data=='salaar'):
        htmldata={
            'name':"Salaar",
            'information':'Salaar: Part 1 – Ceasefire  is a 2023 Indian Telugu-language epic action thriller film written and directed by Prashanth Neel and produced by Vijay Kiragandur under Hombale Films. The film stars Prabhas as the title character alongside an ensemble cast of Prithviraj Sukumaran, Shruti Haasan, Jagapathi Babu, Bobby Simha and Sriya Reddy. In the fictional dystopian city-state of Khansaar, where monarchy still exists, the film follows the friendship between Deva (Prabhas), the exiled prince of Khansaar, and Varadha (Prithviraj Sukumaran), the current prince of Khansaar.',
            'imsrc':'IMAGES/Salaar.jpeg'
        }
    elif(data=='chatrapati'):
        htmldata={
            'name':"Chatrapati",
            'information':'Chatrapathi is a 2005 Indian Telugu-language action film directed by S. S. Rajamouli, who also co-wrote the film with V. Vijayendra Prasad. The film stars Prabhas, Shriya Saran and Bhanupriya alongside Shafi and Pradeep Rawat playing supporting roles. M. M. Keeravani composed the music. The film was produced by B. V. S. N. Prasad on Sri Venkateswara Cine Chitra banner.Chatrapathi was released on 29 September 2005 and emerged as a blockbuster, collecting an estimated distributors share of ₹21 crore ($5 million) against a budget of ₹12.5 crore',
            'imsrc':'IMAGES/chatrapati.jpeg'
        }  
    htmldata['category']='Movies'                       
    return render(request,'news.html',htmldata)    

