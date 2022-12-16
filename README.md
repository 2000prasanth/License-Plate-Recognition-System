# License-Plate-Recognition-System
Developed using python. This code can use camera to capture the picture of a car with license plate and use image processing to extract number plate details from the image. Saves the number plate along with time and status to a MySQL database as sepcified 
AUTOMATIC  LICENSE PLATE RECOGNITION 				       	SYSTEM
PROJECT REPORT
Submitted by
PRASANTH  KV (HGW19CS008)
SAJAL SAUMIAN (HGW19CS009)
TENZIN TSUGMEY (HGW19CS012)
to
the APJ Abdul Kalam Technological University
in partial fulfillment of the requirement for the award of the Degree  
of
Bachelor of Technology
in
Computer Science and Engineering

Department of Computer Science and Engineering
Holy Grace Academy of Engineering  Mala
SEPTEMBER 2022
  
   DECLARATION
We undersigned hereby declare that the project report “Automatic License Plate Recognition System”, submitted for partial fulfillment of the requirement for the award of degree of Bachelor of Technology of the APJ Abdul Kalam Technological University, Kerala is a bonafide work done by us under supervision of Ms. Minu Mohan. This submission represents our ideas in our own words and where ideas or words of others have been included, we have adequately and accurately cited and referenced the original sources. We also declare that we have adhered to ethics of academics honesty and integrity and have not misrepresented or fabricated any data or idea or fact or source in our submission. We understand that any violation of above will be a cause for disciplinary action by the institute and or the university and can also evoke penal action from the sources which have thus not been properly cited or from whom proper permission has not been obtained. This report has not been previously formed the basis for the award of any degree, diploma or similar title of any other University.

Place: Mala  
Date:

DEPARTMENT OF COMPUTER SCIENCE 				                       AND ENGINEERING
HOLY GRACE ACADEMY OF ENGINEERING, MALA

CERTIFICATE
This is to certify that the report entitled ‘Automatic License Plate Recognition System’ submitted by “Prasanth KV, Sajal Saumian, Tenzin Tsugmey” to the APJ Abdul Kalam Technological University in partial fulfillment of the requirements for the award of the Degree of Bachelor of Technology in Computer Science and Engineering, is a bonafide record of the work carried out by him/her under our guidance and supervision. This report in any form has not been submitted to any other    university or institute for any purpose.
        INTERNAL SUPERVISOR                           EXTERNAL SUPERVISOR
            Ms. Minu Mohan
            Assistant Professor
            Dept Of  CSE

            PROJECT COORDINATOR                          HEAD OF DEPARTMENT
            Ms. Soosan Francis                                          Ms. Rinsu Aravind
            Assistant Professor                                           Assistant Professor
            Dept Of  CSE           				  Dept  Of CSE

ACKNOWLEDGEMENT

We are greatly indebted to Dr. G. Harikrishnan, Principal, Holy Grace Academy of Engineering, Mala ,Ms Rinsu Aravind, Head Of Department Computer Science Engineering, Ms. Minu Mohan our project guide, Department of Computer Science and Engineering, Ms Soosan Francis our project coordinator, Department of Computer Science, Holy Grace Academy of Engineering, who wholeheartedly granted us permission to carry out the project and for the valuable guidance and support.
We would like to express our sincere gratitude to all the teachers of the Computer Science Department who gave us moral and technical support. We would like to thank the supporting staff in the computer lab whose dedicated work kept the lab working smoothly, thus enabling us to have access to various resources which helped us understand more about the project topic. We would also like to thank my friends and family members for providing us with the necessary resources and support. Last but not least, we would like to thank God Almighty for helping us to conduct the project hassle free.

 ABSTRACT

We will be using the OpenCV Library to detect and recognize faces and alphanumeric digits. License Plate Detection - The first step is to detect the License plate from the car. We will use the contour option in OpenCV to detect for rectangular objects to find the number plate. The accuracy can be improved if we know the exact size, color and approximate location of the number plate. Normally the detection algorithm is trained based on the position of camera and type of number plate used in that particular country. This gets trickier if the image does not even have a car, in this case we will an additional step to detect the car and then the license plate. Character Segmentation - Once we have detected the License Plate we have to crop it out and save it as a new image. Again this can be done easily using OpenCV. Gray-scaling is done on the image and contours are detected (A contour line of a function of two variables is a curve along which the function has a constant value, so that the curve joins points of equal value ) then the image is passed for OCR processing. Character Recognition - Now, the new image that we obtained in the previous step is sure to have some characters (Numbers/Alphabets) written on it. so, we can perform OCR (Optical Character Recognition) on it to detect the number. We use pytesseract OCR module as  OCR engine. 
AUTOMATIC LICENSE PLATE DETECTION is a computer vision technology to extract license no of vehicles from images. Typical implementation using propriety technologies tend to be costly. Here we use OpenCV(Open Computer Vision) for implementing the system. Specific implementation of this system for a car parking management is done here.



CONTENTS
DECLARATION										ii
CERTIFICATE										iii
ACKNOWLEDGEMENT								iv
ABSTRACT										v
LIST OF FIGURES									x
ABBREVIATIONS									xi
Chapter 1
INTRODUCTION
1.1  Definition 										1
1.2  Purpose and scope									2
1.3  Product perspectives									3
1.4  Constraints										3
Chapter 2
 LITERATURE REVIEW
2.1  Automatic Number Plate recognition using Raspberry P I 				5
2.2  Image Corner Detection Using Hough Transform					6
2.3  Algorithmic And Mathematical Principles Of ALPR				7
2.4  Automatic License Plate Recognition using OpenCV				8
2.5  A License Plate recognition Algorithm For Intelligent Transport System          	9
2.6  A Complete System For Vehicle Plate Localization, Segmentation and                 10 recognition in real life scenario						           
Chapter 3
SYSTEM ANALYSIS
3.1 UI design											11
3.2 Functional requirements								12
3.3 Software requirements									12
3.4 Hardware requirements									14
3.5 Non- Functional requirements								15
Chapter 4 
METHODOLOGY
4.1 Algorithm										            17
4.2 Proposed system										17

Chapter 5
SYSTEM DESIGN
5.1 Class Diagrams										18
5.2 Sequence Diagrams									19
5.3 State Diagrams										20
5.4 ER Diagrams										21
5.5 Activity Diagrams									22
5.6 Use- Case Diagrams									23
Chapter 6 
SYSTEM IMPLEMENTATION							24
Chapter 7
TESTING
7.1 Test-case report  									  	25
7.2  OpenCV vs MATLAB                                                                                                   25
7.3  Modular Testing										26
7.4  Reliability Testing							    		27
Chapter 8
RESULTS											28
Chapter 9 
CONCLUSION										31
REFERENCES										32
CODE																						 	33


















LIST OF FIGURES

NO	TITLE	Page no
3.1	USER-INTERFACE	11
5.1	CLASS DIAGRAM	18
5.2	SEQUENCE DIAGRAM	19
5.3	STATE-CHART DIAGRAM	20
5.4	ER DIAGRAM	21
5.5	ACTIVITY DIAGRAM	22
5.6	USE-CASE DIAGRAM	23
8.1	CLICKING IMAGE	28
8.2	UI	29
8.3	DATABASE	30







ABBREVIATIONS

ALPR	Automatic License Plate Recognition
ANPR	Automatic Number Plate Recognition
Open CV	Open Computer Vision
OCR	Optical Character Recognition
AI	Artificial Intelligence
ML	Machine Learning
PIL	Pillow module
DBMS	Database Management System


CHAPTER 1
INTRODUCTION
1.1  Definition
The License Plate Recognition System recognizes the vehicle number plate from a given image using image segmentation and Optical Character Recognition and stores the extracted alphanumeric string in the provided LPR database.
The scientific world is deploying research in intelligent transportation systems which have a significant impact on peoples´ lives. Automatic License Plate Recognition (ALPR) is a computer vision technology to extract the license number of vehicles from images. It is an embedded system which has numerous applications and challenges.
 Typical ALPR systems are implemented using proprietary technologies and hence are costly. This closed approach also prevents further research and development of the system. With the rise of free and open source technologies the computing world is lifted to new heights. People from different communities interact in a multi-cultural environment to develop solutions for mans never ending problems. 
One of the notable contribution of the open source community to the scientific world is Python. Intel’s researches in Computer Vision bore the fruit called Open Computer Vision (OpenCV) library, which can support computer vision development.

1.2 Purpose and Scope
The purpose of this project is to develop a Computer Vision system using python and OpenCV that enables a larger system to distinguish vehicle number plates and extract characters with minimum error. This system can be embedded with Larger security systems, Automatic parking systems, AI vehicles etc.
ANPR technology has surged in popularity in recent years due to its wide range of benefits for various applications like traffic management, intelligent parking, toll automation, intelligent transportation systems in smart cities, and journey time analysis are just a few of the advantages that ANPR offers.
An automatic license plate recognition system can be used for a variety of purposes, such as tracking the movement of vehicles, identifying specific cars, automated parking enforcement, and so on. The use of ANPR systems is becoming more popular as the technology advances rapidly with the advent of machine learning and deep learning, the computational cost decreases, and the accuracy of applied image processing techniques increases.
Recent innovations have contributed to the adoption of ANPR for perimeter security and access control applications at government facilities. Within the US, "homeland security" efforts to protect against alleged "acts of terrorism" have resulted in adoption of ANPR for sensitive facilities such as embassies, schools, airports, maritime ports, military and federal buildings, law enforcement and government facilities, and transportation centers. ANPR is marketed as able to be implemented through networks of IP based surveillance cameras that perform "double duty" alongside facial recognition.
Real-time object detection Object detection uses deep learning to recognize vehicles and different vehicle classes (bus, truck, car, van, motorcycle, etc.) in images of video streams. State-of-the-art object detection algorithms such as YOLOv3 or YOLOv7 use neural networks trained on a data-set of images.

1.3 Product Perspective
The scientific world is deploying research in intelligent  transportation systems which have a
significant impact on peoples lives. Automatic License Plate Recognition (ALPR) is a computer vision technology to extract the license number of vehicles from images. It is an embedded system which has numerous applications and challenges. 
Typical ALPR systems are implemented using proprietary technologies and hence are costly. This closed approach also prevents further research and development of the system With the rise of free and open source technologies the computing world is lifted to new heights. People from different communities interact in a multi-cultural environment to develop solutions for man’s never ending problems.
One of the notable contribution of the open source community to the scientific world is Python. Intel’s researches in Computer Vision bore the fruit called Open Computer Vision (OpenCV) library, which can support computer vision development. Here this system is implemented as a parking system where the number plate information, Time of vehicle arrival, Date etc is stored in a data structure within the python program which is later uploaded to the Database.

1.4  Constraints
1. Diverse environmental effects like fog, rain ,dust etc can potentially confuse the OCR system.
2. Angle of frame, Number of vehicles etc may cause irregularities.
3. Excessive sunlight can disturb identification of contours within the image The system    works best at modest to low brightness.
4. License plates which do not have bold clear boundary marking can lead to irregularities in detecting contours.
5. The system gives best results when working with dark colored cars since it can easily identify contours in the given scenario.
6. The system doesn’t work for square plates since decoding the two layer of data is not added.
7. Due to the current system having limited computing power implementing TensorFlow machine learning module might crash the system so we are sticking with pytesseract – Tesseract OCR engine.
8. Poor file resolution, usually because the plate is too far away but sometimes resulting from the use of a low-quality camera.
9. A different font, popular for vanity plates (some countries do not allow such plates, eliminating the problem)
10. Lack of coordination between countries or states. Two cars from different countries or states can have the same number but different design of the plate.
11. An object obscuring (part of) the plate, quite often a tow bar, or dirt on the plate







CHAPTER 2
LITERATURE REVIEW
2.1  Automatic Number Plate recognition using Raspberry Pi [1]
ALPR acknowledges the vehicle number plate. ALPR extracts ASCII characters from images automatically. Raspberry Pi is  a low cost portable System on Chip PC . The Raspberry Pi is a very low-cost computer that runs Linux and has a set of input and output pins that allow users to control electronic components
License Plate Recognition System using Raspberry Pi and Pi Camera. This system automatically recognizes and reads vehicle license plates using OpenCV and Optical Character Recognition. Pi camera module continuously captures the frames, and when a key is pressed on the keyboard, it saves the last frame as a new image.
Then it uses the contour function from OpenCV to detect the license plate. And finally, Raspberry Pi crops out that particular area and perform optical character recognition to read the license plate numbers.
CONCLUSION 
We conclude that  the ALPR system can effectively recognize number plate region and extract ASCII characters from it 
 DISADVANTAGES :  Raspberry Pi is a device with very low computing power, Installing complex software like Open-CV, OCR engines etc, can potentially make it unstable. It would require an high end version of Raspberry Pi and a robust cooling system to support the main system.


2.2  Image Corner Detection Using Hough Transform [2]
The basic idea is to find the straight lines in the images and then search for their intersections, which are the corner points of the objects in the images. The Hough Transform is used for detecting the straight lines and the inverse Hough Transform is used for locating the intersection points among the straight lines, and hence determine the corner points.  Ideally, a corner is an intersection of two straight lines. However, in practice, corners in the real world are frequently deformed with ambiguous shapes. As corner represent certain local graphic features at abstract level, corners can intuitively be described by some semantic patterns. 
 Type A: A perfect corner as modeled in  i.e., a sharp turn of curve with  smooth parts on both sides.  
Type B: The first of two connected corners similar to the END or STAIR models in  i.e., a mark of change from a smooth part to a curved part.
Type C: The second of two connected corners, i.e., a mark of change from a curved part to a smooth part. 
Type D: A deformed model of type A, such as a round corner or a corner with arms neither long nor smooth. The final interpretation of the point may depend on the high level global interpretation of the shape. 
ADVANTAGES : In most of the scenarios number plate detection fail because of irregularities in corner – edge detection we can overcome this through Hough  transform. 
DISADVANTAGES: doesn’t work on those edges which doesn’t fall under the give four categories, low contrast etc.


2.3  Algorithmic And Mathematical Principles Of ALPR [3]
This work deals with Artificial Intelligence, Machine Vision and neural networks in construction of an automatic number plate recognition system , Mathematical aspects , for a machine number plate is only a gray picture defined by two dimensional function f(x,y) . Problematic areas of ALPR include algorithms which are able to detect a rectangular area as a number plate. Principles of character recognition include character segmentation using horizontal projection of a pre-processed number plate, But if irregularities still exists more sophisticated algorithms can be used , Character dimensions and brightness must be normalized.
The feature extraction algorithm must be applied on characters to filter irrelevant data. It is necessary to extract features which will be invariant towards all types of character deformations We can use pattern classifier and neural networks and deal with their usage in recognition of characters , Characters can be classified and recognized by simple nearest neighbor algorithm(INN) applied to vector extraction features. 
We can use heuristic analysis which are used to eliminate non character elements from plate A number ‘O’ can be inferred as ‘0’ , this can be repaired with a character ‘O’ on positions where numbers are not allowed . Heuristic analysis is easy to implement and can be implemented using python string functions.
CONCLUSION: Here we conclude that the above three algorithms can help improve the precision of license plate recognition many-folds. 
DISADVANTAGE:  Highly complex algorithm, implementation of the above given three algorithms require robust trial and error testing. Implementing the above system needs a high end machine and development environment.


2.4  Automatic License Plate Recognition using OpenCV [4]
AUTOMATIC LICENSE PLATE DETECTION is a computer vision technology to  extract license no of vehicles from images. Typical implementation using  propriety technologies tend to be costly. Here we use OpenCV(Open Computer Vision) for implementing the system. Specific implementation of  this system for a car parking management is done in this project Gaussian blur is the  result of blurring an image by a Gaussian function then detect the edges  using canny function.
 Canny Edge Detection is used to detect the edges in  an image. It accepts a gray scale image as input and it uses a multistage algorithm and Reduce Noise using Gaussian Smoothing.
 The system captures an image of a vehicle, Processes the image , masks the number plate and extracts the vehicle number as string using pytesseratct OCR module. 
Recent innovations have contributed to the adoption of ANPR for perimeter security and access control applications at government facilities. Within the US, "homeland security" efforts to protect against alleged "acts of terrorism" have resulted in adoption of ANPR for sensitive facilities such as embassies, schools, airports, maritime ports, military and federal buildings, law enforcement and government facilities, and transportation centers. ANPR is marketed as able to be implemented through networks of IP based surveillance cameras that perform "double duty" alongside facial recognition.
ADVANTAGES :  It uses robust image processing by implementing OpenCV image functions  Pytesseract module takes less memory and CPU hence reduce sluggishness.  
DISADVANTAGES : Pytesseract OCR is less accurate when dealing with numbers  Image processing algorithm might not be able to find contours when exposed to rain,fog, excessive sunlight etc.


2.5  A License Plate recognition Algorithm For Intelligent 	Transport  System [5]
A new algorithm for vehicle License plate identification is proposed. On the basis of a novel adaptive image segmentation technique & connected component analysis in conjunction with character recognition neural network .  During recent times Intelligent transportation systems are having a wide impact on people’s lives since they have scope to improve transportation safety and mobility , license plates remain the principle vehicle identifier despite the fact that it can be deliberately altered. The focus here is to integrate a novel segmentation technique implemented in LPR to cope with outdoor conditions , a novel segmentation technique named sliding concentric window is used for faster detection of region of Interest .An algorithmic sequence able to cope with plates of various sizes and positions. More than one license plate can be segmented in the same image. 
 A: License plate segmentation 
This is done with the hope that the subsequent stage of recognition, focused on the license plate alone, could require less data, due to the reduced dimensions of the input, for a given model complexity with a high precision.
 B: License plate processing 
A segmentation model is used to crop all the training images. The cropped images and the corresponding manually labeled text is used to train a custom OCR model, to get the text (numbers and letters) of the license plate for each input image.
 C: Character Recognition
An OCR program extracts and re-purposes data from scanned documents, camera images and image-only pdfs. OCR software singles out letters on the image, puts them into words and then puts the words into sentences, thus enabling access to and editing of the original content.


2.6  A Complete System For Vehicle Plate Localization, 	Segmentation and recognition in real life scenario [6]
There are many applications of ALPR , from complex security systems to parking admissions etc. Car License plate detection has complex characteristics due to diverse effects such as fog , rain, shadows, car’s velocity ,angle of frame, number of vehicles etc. 
These factors make plate recognition much more complex and difficult than the traditional pattern or optical character recognition (OCR) systems. The main objective of this work is to show a system that solves the practical problem of car identification for real scenes. All steps of the process, from image scene acquisition to optical character recognition are considered to achieve an automatic identification of plates.
It can be used with all type of country rules or plates design and adapted to each situation. The system is computationally very efficient and it is suitable for others related image recognition applications.
CONCLUSION : We conclude the above factors make plate recognition more complex and less accurate.
This paper proposes a system to solve the above irregularities. All steps of process from image scene recognition to OCR are considered to achieve identification of plates which can be used with all types of national protocols or plate design, without reducing system’s computational efficiency.




CHAPTER  3
SYSTEM  ANALYSIS
3.1  UI Design
The aim here is to activate camera input by user command (SPACBAR),  The camera window is closed when ESC is pressed. The camera clicks image of given car number plate and processes the image, character recognition is done in the same window specified and extracted license plate number is displayed to the user. The License plate info along with corresponding date and time is stored and can be further accessed by the user in the corresponding mySQL database .A Database view LPR-VEHICLE is created to display the data stored in the database.

					Fig 3.1: User-Interface

3.2  Functional Requirements
FR 1: The Software should be able to correctly detect and crop the part of the image containing number Plate with minimum error.
FR 2: The Software should be able to gray scale the cropped image to reduce anomalies in OCR process.
FR 3: OCR function should be able to extract ASCII characters and digits with maximum precision.
FR 4: Efficiently store vehicle identification information in the databases.
FR 5 : The system must have a functional UI.
FR 6: The system should be quick in identifying and storing the number plate information.
FR 7: The system must be able to capture the image correctly.
FR 8: The system must correctly write the captured file into ‘opencv.png’.
FR 9: The rewritten file must  not get corrupted.
FR 10: The database must store DATE, TIME information corresponding to the license number. 

3.3  Software Requirements
The software aspect of the system runs on standard home computer hardware and can be linked to other applications or databases. It first uses a series of image manipulation techniques to detect, normalize and enhance the image of the number plate, and then optical character recognition (OCR) to extract the alphanumeric characters of the license plate. 

ANPR systems are generally deployed in one of two basic approaches: one allows for the entire process to be performed at the lane location in real-time, and the other transmits all the images from many lanes to a remote computer location and performs the OCR process there at some later point in time. When done at the lane site, the information captured of the plate alphanumeric, date-time, lane identification, and any other information required is completed in approximately 250 milliseconds.[citation needed] This information can easily be transmitted to a remote computer for further processing if necessary, or stored at the lane for later retrieval. In the other arrangement, there are typically large numbers of PCs used in a server farm to handle high workloads, such as those found in the London congestion charge project. Often in such systems, there is a requirement to forward images to the remote server, and this can require larger bandwidth transmission media.
OpenCV : Is Expanded as Open Computer Vision , it is a cross-platform library using which we can develop real-time computer vision applications. It mainly focuses on image processing, video capture and analysis including features like face detection and object detection. OpenCV is installed in the chosen python Integrated development environment and is used to interpret code. 
Imutils : is a series of convenience functions to make basic image processing functions such as translation, rotation, re-sizing, skeletonization, and displaying Matplotlib images easier with OpenCV and both Python 2.7 and Python 3. 
Numpy : is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python. 
Python-tesseract : is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images. Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.
PIL :  is the Python Imaging Library which provides the python interpreter with image editing capabilities. The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images. 
Tkinter : Graphical User Interface(GUI) is a form of user interface which allows users to interact with computers through visual indicators using items such as icons, menus, windows, etc. Tkinter is the inbuilt python module that is used to create GUI applications. It is one of the most commonly used modules for creating GUI applications in Python. 
Turtle : Turtle  is a Python feature like a drawing board, which lets us command a turtle to draw all over it! We can use functions like turtle.forward(…) and turtle.right(…) etc. 
MySQL-Connector-Python
MySQL Connector/Python enables Python programs to access MySQL databases, using an API that is compliant with the Python Database API Specification v2.0 (PEP 249).

3.4  Hardware Requirements
License plate images while simultaneously doing an alpha numeric conversion of the captured plates. Recent changes in computer processing power and memory combined with lower price points for economies of scale have allowed for real time processing of license plate recognition systems. 

LPR Camera Specifications: 


 The main component of an LPR system is of course, the camera. The camera specifications below are standard criteria required to ensure thorough imaging of a license plate is captured in order to secure your bottom line. 
Standard specifications for LPR cameras mounted on enforcement vehicles are identical to that of cameras located at a parking lot entry and exit. They are commonly referred to as license plate inventory (LPI). 
To maximize the chances of effective license plate capture, installers should carefully consider the positioning of the camera relative to the target capture area. Exceeding threshold angles of incidence between camera lens and license plate will greatly reduce the probability of obtaining usable images due to distortion.
To avoid blurring it is ideal to have the shutter speed of a dedicated camera set to 1/1000 of a second. It is also important that the camera use a global shutter, as opposed to rolling shutter, to assure that the taken images are distortion-free.
Colour camera
1080p, full high definition (HD) resolution
A normal computer system with windows 10 (python 3.0+ models only support windows 10+ operating systems, Mac OS mojave+ or latest version of LINUX-UBUNTU( distribution 2018+) 
CPU SPEED: 1 GHz or faster processor , 2 GB RAM , Dedicated GPU.

3.5  Non - Functional Requirements
Non-functional requirements or NFRs are a set of specifications that describe the system’s operation capabilities and constraints and attempt to improve its functionality. These are basically the requirements that outline how well it will operate including things like speed, security, reliability, data integrity, etc.


NFR1 : The system must be able to load the image directly from the camera module and do the processing using TensorFlow.
NFR2: The system must be able to use Machine learning to overcome irregularities. 
NFR3 : Advanced User Interface.
NFR4 : Using Easy OCR can improve OCR accuracy but it’s implementation is resource intensive.
NFR5: Storing Database data in an external server for universal-secure access.
NFR 6: Remote access of database data.
NFR 7: Time complexity of code.










				CHAPTER 4
				    METHODOLOGY
4.1  Proposed system
Our Proposed License Plate Recognition system takes the image of the vehicle as input  Process the image Gray-scaling, applying Gaussian blur, Detecting edges,masking the number plate and the image is send to pytesseract OCR for extracting the number from the image .  Pytesseract OCR is an open-source version of Google’s Tesseract  OCR engine which is continuously updated by google. The proposed system relies on moderate to heavy image processing. The contour defined as number plate is passed onto the pytesseract OCR engine and number plate is extracted as name_text. The vehicle number along with current time and date is inserted into the database and the user can edit details, retrieve data etc from the LPR database.
4.2  Algorithm
Step1: Start
Step 2: Capture Image
Step 3: Grayscale Image an crop
Step 4 : Detect Contours in image
Step 5: Extract contours similar to number plate characteristics
Step 6: Perform OCR on the Number_plate
Step 7: Extract Number plate as name_text string
Step 8: Store Number_plate along with date and time in the LPR database
Step 9: Stop

CHAPTER 5
SYSTEM DESIGN
5.1  Class diagram
The class diagram is one of the types of UML diagrams which is used to represent the static diagram by mapping the structure of the systems using classes, attributes, relations, and operations between the various objects. 
In object-oriented programming, a class is an extensible program-code-template for creating objects, providing initial values for state and implementations of behavior.
A class diagram has various classes; each has three-part; the first partition contains a Class name which is the name of the class or entity which is participated in the activity, the Second partition contains class attributes that show the various properties of the class, the third partition contains class operations which shows various operations performed by the class, relationships shows the relation between two classes
					Fig 5.1: Class Diagram


5.2  Sequence Diagram 
 Sequence Diagrams are interaction diagrams that detail how operations are carried out. They capture the interaction between objects in the context of a collaboration. 
Sequence Diagrams are time focus and they show the order of the interaction visually by using the vertical axis of the diagram to represent time what messages are sent.
Sequence Diagrams show elements as they interact over time and they are organized according to object (horizontally) and time (vertically).


                   		   Fig 5.2: Sequence diagram

5.3  State Chart Diagrams 
 A state diagram shows the behavior of classes in response to external stimuli. Specifically a state diagram describes the behavior of a single object in response to a series of events in a system.
 Sometimes it's also known as a Harel state chart or a state machine diagram. This UML diagram models the dynamic flow of control from state to state of a particular object within a system.
State-chart diagram defines the states of a component and these state changes are dynamic in nature. Its specific purpose is to define the state changes triggered by events. Events are internal or external factors influencing the system.
				

Fig 5.3: State chart diagram


5.4    ER Diagram 
Stands for Entity Relationship Diagram, also known as ERD is a diagram that displays the relationship of entity sets stored in a database. In other words, ER diagrams help to explain the logical structure of databases.
 ER diagrams are created based on three basic concepts: entities, attributes and relationships. ER Diagrams contain different symbols that use rectangles to represent entities, ovals to define attributes and diamond shapes to represent relationships.
ER model helps to systematically analyze data requirements to produce a well-designed database. The ER Model represents real-world entities and the relationships between them. Creating an ER Model in DBMS is considered as a best practice before implementing your database.
ER Modeling helps you to analyze data requirements systematically to produce a well-designed database. So, it is considered a best practice to complete ER modeling before implementing your database.






			       Fig 5.4: Entity Relationship Diagram
   


5.5  Activity Diagram
Activity Diagram describe how activities are coordinated to provide a service which can be at different levels of abstraction. Typically, an event needs to be achieved by some operations, particularly where the operation is intended to achieve a number of different things that require coordination, or how the events in a single use case relate to one another, in particular, use cases where activities may overlap and require coordination. It is also suitable for modeling how a collection of us cases coordinate to represent business workflows.
  				   Fig 5.5: Activity diagram

5.6 Use-Case Diagram
A use case diagram is a graphical depiction of a user's possible interactions with a system. A use case diagram shows various use cases and different types of users the system has and will often be accompanied by other types of diagrams as well. The use cases are represented by either circles or ellipses. The actors are often shown as stick figures. 














Fig 5.6: Use-Case diagram


CHAPTER 6
SYSTEM IMPLEMENTATION
Implementation is the process that actually yields the lowest-level system elements in the system hierarchy (system breakdown structure). System elements are made, bought, or reused. Production involves the hardware fabrication processes of forming, removing, joining, and finishing, the software realization processes of coding and testing, or the operational procedures development processes for operators' roles. If implementation involves a production process, a manufacturing system which uses the established technical and management processes may be required.
The Automatic License Plate Recognition system is implemented in Visual Studio Code using Python and is saved a ‘final.py’ . The image clicked using the Capture() function is saved as ‘opencv.png’ (png uses minimum compression as compared to JPEG).
The opencv.png image is loaded. Grayscaling and cropping is performed using OpenCV and the edged image is loaded using Canny() function (Canny function highlights intensity variations in an image).  Contours in the edged image is detected and the masked number plate is processed using pytesseract Optical Character Recognition module to extract characters/numbers from the masked License Plate image.
The License Plate along with DATE and TIME is stored into ‘LPR’ database.  Database is implemented using mySQL 8.0 workbench and is accessed using a SELECT query from the table ‘vehicle’.



CHAPTER 7
TESTING
7.1 Test-case Report
1. The License Plate Recognition System was first tested against various  lighting scenarios and the following observations were made. The system showed inconsistent results when exposed to bright light, bright light makes it harder to detect edges correctly. The system works best in low daylight , when the number plate is visible and edges are not blurred.
2. The system showed inconsistent results when exposed to white car’s because  it is harder to    detect the edge between white number-plate against a white background when the frame is not thick enough. the system works fine for cars of colors like, red, black, gray etc.
3.  The database connects with the system well and stores the result as expected.
4. The UI worked as expected.
5. Debugging : Many of the standard debugging operations can be used with both Matlab and OpenCV: breakpoints can be added to code, the execution of lines can be stepped through, variable values can be viewed during code execution etc. 

7.2  OpenCV comparison with MATLAB
From the final scores we can see that OpenCV has the edge over Matlab for image and video processing development . Although Matlab has an easy learning curve, built in memory management, a great help section, it is very slow to execute code, and is expensive to get started in. While OpenCV can be difficult to debug and requires much “housework code” needed for memory management, header files, etc., it wins out due to its free cost, the magnitude of sample code available on the internet, the short development path from prototype code to embedding code, the useful programming skills learnt from its use, and its super-fast speed.

OpenCV is the most comprehensive open source library for computer vision and it has large user community. OpenCV has more functions for computer vision than Matlab. Many of its functions are implemented on GPU. The library is being continuously updated (an updated version is released approximately every 3 to 4 months). In general C++ OpenCV code runs faster than Matlab code (if it's not fast enough, you can make it faster by optimizing the source code).
Matlab is useful for rapid prototyping and Matlab code is very easy to debug. It has good documentation and support. However, as others have mentioned, Matlab is not open source, its licence is pretty pricey, and its programs are not portable. Matlab is an interpreted language and it negatively affects its performance. Performance matters a lot in computer vision.

7.3  Modular Testing
Module testing is defined as a software testing type, which checks individual subprograms, subroutines, classes, or procedures in a program. Instead of testing whole software program at once, module testing recommends testing the smaller building blocks of the program.
The test for Capture() module worked as expected., The module successfully captured the image when SPACE was pressed and the window closed when ESC was pressed the file was successfully written on to ‘opencv.png’.
The test for Image processing worked as expected : The module successfully gray-scaled and cropped the image, The edges where extracted and correct contour of the number plate was detected successfully. Pytesseract  module extracted the license number as string.
The test for UI worked as expected, the UI displayed the license number to the user.

The test for Database worked as expected, the database successfully established connection with the python program and it stored the python-DATE, python-TIME in the LPR database.

7.4  Reliability Testing
Reliability is defined as the probability of failure-free software operation for a specified period of time in a particular environment. Reliability testing is performed to ensure that the software is reliable, it satisfies the purpose for which it is made, for a specified amount of time in a given environment and is capable of rendering a fault-free operation.
The Automatic License Plate Recognition system is tested reliable in daylight conditions and when given conditions are satisfied.
When there are no irregularities like
1.Irregular Angle of frame.
2. License plates which do not have bold clear boundary. 
3.When the plate give is square.or two layered license plate.
4.Captured image is not blurry.
5.Captured image does not have a balanced contrast.
6. The object (car/vehicle) is not in focus.






CHAPTER 8
RESULTS
Clicking image
-
		          		           Fig 8.1: clicking image
The image is captured when SPACE is pressed  and the capture UI is closed when ESC(Escape) is pressed




UI


				Fig 8.2: User-Interface of ALPR








Database


			  Fig 8.3: Database view in MySQL 8.0

SQL  QUERY TO ACCESS DATA :
USE LPR ;
SELECT * FROM VEHICLE ;



CHAPTER  9
CONCLUSION
The Automatic number plate recognition system has been implemented. The implemented system takes the image of the Vehicle as input from the user using the capture() method and effectively recognizes the number plate region in the image which consists of vehicle number. This algorithm is applied on several images and observed that it works successfully. The main objective to implement the system is to recognize the number plates of the vehicles in order to replace the current system of manual entry in security purpose. This system was a success in detecting the number plate of a vehicle. The extracted number along with date, time when the image was clicked and the current status detail are stored onto the ‘LPR’ database specified and is made available for future references.










 REFERENCES
1.Sajjad, K.M .: “Automatic license plate recognition using python ,OpenCV and. Raspberry Pi” Department of Computer Science and Engineering, MES College of Engineering, Kuttippuram, Kerala (2010).
2.Sung Kwan Kang,Young Chul Choung,and Jong An Park: “Image Corner Detection Using Hough Transform”
3..  Ondrej Martinsky (2007). "Algorithmic and mathematical principles of automatic number plate recognition systems" (PDF). Brno University of Technology.
4.Pratiksha Jain, Neha Chopra and Vaishali Gupta .: Automatic License Plate Recognition using OpenCV .International Journal of Computer Applications Technology and Research Volume
5.Ahmed Gull Liaqat, “Real Time Mobile License Plate Recognition System” IEEE White paper California, VOL.2 2011-12-05,Linnaeus University.
6.. A. Conci, J. E. R. de Carvalho, T. W. Rauber, “ A Complete System for Vehicle Plate Localization, Segmentation and Recognition in Real Life Scene” , IEEE LATIN AMERICA TRANSACTIONS, VOL. 7, NO. 5,SEPTEMBER 2009
7.Mousa, A . : Canny edge-detection based vehicle plate recognition.International Journal of signal processing, Image processing and pattern recognition, . 5(3), pp.1-8(2012).
8.Buhus, E.R., Timis, D. and Apatean, A .:Automatic parking access using openalpr on raspberry pi3. Acta Technica Napocensis. 57(3), p.10 (2016) .
9.Fukunaga K.: Introduction to statistical pattern recognition, Academic Press, San Diego, USA, 1990






root.mainloop()
