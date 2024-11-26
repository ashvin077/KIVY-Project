from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.core.window import Window

# import requests
# from kivymd.uix.button import MDRectangleFlatButton

Window.size = (350, 650)

KV = """
ScreenManager:
    MainScreen:
    MaleWorkouts:
    FemaleWorkouts:
    MaleAbsWorkouts:
    MaleLegWorkouts:
    MaleChestWorkouts:
    MaleShoulderWorkouts:
    MaleBackWorkouts:
    MaleThighWorkouts:
    MaleArmsWorkouts:
    MaleBicepsWorkouts:
    MaleNeckWorkouts:
    FemaleAbsWorkouts:
    FemaleLegWorkouts:
    FemaleChestWorkouts:
    FemaleShoulderWorkouts:
    FemaleBackWorkouts:
    FemaleThighWorkouts:
    FemaleArmsWorkouts:
    FemaleGlutesWorkouts:
    FemaleNeckWorkouts:

<MainScreen>
    name: 'mainscreen'
    MDBoxLayout:
        orientation: "vertical"
    
        MDBottomNavigation:
            panel_color: '#aaabaa'
            text_color_normal: "#000000"
            selected_color_background: '#ffffff'
            text_color_active: "#000000"
    
            MDBottomNavigationItem:
                name: "screen1"
                text: "Home"
                icon: 'home-account'
    
                MDCard:
                    style: "elevated"
                    pos_hint: {"center_x":.5, "center_y":0.9}
                    theme_shadow_color: "Custom"
                    size_hint_x: 1                              # Fit the width of the screen
                    size_hint_y: 0.3
                    # height: "200dp"
                    # orientation: "vertical"
                    shadow_color: '#9850a1'
                    theme_bg_color: 'Custom'
                    md_bg_color: "#131313"
                    padding: '20dp','39dp','0dp','0dp'
    
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: '0dp'  # Ensures no space between labels
                        padding: '10dp'
                        spacing: '20dp'
    
                        MDLabel:
                            text: "Hello There!"
                            halign: "justify"
                            color: "white"
                            font_size: '25dp'
                            bold: True
                        MDLabel:
                            text: "Welcome to your fitness journey"
                            halign: "left"
                            color: "white"
                            font_size: '22dp'
                            bold: True
                        MDLabel:
                            text: "Be healthy and get desired shape for your body."
                            halign: "justify"
                            color: "white"
                            font_size: '15dp'
                            bold: True
    
            MDBottomNavigationItem:
                name: "screen2"
                text: "workouts"
                icon: 'dumbbell'
            
                MDCard:
                    style: 'elevated'
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    theme_bg_color: 'Custom'
                    md_bg_color: '#ffffff'
                    size_hint_x: 1
                    size_hint_y: 1
                    radius: [0,0,0,0]
                
                MDCard:
                    style: 'elevated'
                    pos_hint: {'center_x':0.5, 'center_y':0.9}
                    theme_bg_color: 'Custom'
                    md_bg_color: '#ffffff'
                    size_hint_x: 1
                    size_hint_y: 0.4
                    background: "Images/Leg.jpg"
                    padding: '20dp'
                    MDLabel:
                        text:'Select Your Exercise Here'
                        color:'#ffffff'
                        bold: True
                        pos_hint: {'center_y':0.1}
                        font_size: '23dp'
                
                MDCard:
                    style: 'filled'
                    pos_hint: {'center_x':0.5, 'center_y':0.525}
                    theme_bg_color: 'Custom'
                    md_bg_color: '#131313'
                    size_hint_x: 1
                    size_hint_y: 0.3
                    radius: [50,0,50,0]
                    padding: '20dp'
                    BoxLayout:
                        orientation: 'vertical'
                        MDLabel:
                            text: 'Essentials to Know Before You Exercise'
                            bold: True
                            color: '#ffffff'
                            pos_hint: {'center_x':0.5, 'center_y':0.8}
                        MDLabel:
                            text: '1) Make Sure Your are hydrated.'
                            color: '#ffffff'
                            pos_hint: {'center_x':0.5, 'center_y':0.7}
                        MDLabel:
                            text: '2) Spend at least 5–10 minutes warming up'
                            color: '#ffffff'
                            pos_hint: {'center_x':0.5, 'center_y':0.5}
                        MDLabel:
                            text: '3) Make Mind Strong and get started..'
                            color: '#ffffff'
                            pos_hint: {'center_x':0.5, 'center_y':0.3}
                            
                MDCard:
                    style: 'filled'
                    pos_hint: {'center_x':0.25, 'center_y':0.19}
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.35
                    size_hint_y: 0.3
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_card_press("male_workouts")  # Call function when the card is pressed
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage:
                            source: "Images/male_workout.jpg"
                            radius: [10,10,10,10]
                            size_hint_y: 0.6             # Adjust height proportionally to card
                            pos_hint: {'center_x':0.5, 'center_y':0.65}
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel: 
                                text: 'Male'
                                bold: True
                                color: '#ffffff'
                                font_style: 'H6'
                                pos_hint: {'center_x':0.5, 'center_y':0.2}
                                
                MDCard:
                    style: 'filled'
                    pos_hint: {'center_x':0.75, 'center_y':0.19}
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.35
                    size_hint_y: 0.3
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_card_press("female_workouts")  # Call function when the card is pressed
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/female_workout.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Female"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                                
                                
    
            MDBottomNavigationItem:
                name: "screen3"
                text: "Goals"
                icon: 'chart-bar'
    
                MDLabel:
                    text: 'Goals'
                    halign: 'center'
                    
                    
    
            MDBottomNavigationItem:
                name: "screen4"
                text: "Profile"
                icon: 'account-circle-outline' 
                MDCard:
                    style: 'elevated'
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    md_bg_color: '#000000'
                    radius: [0, 0, 0, 0]
                    MDLabel:
                        text: 'Hello There!'
                        halign: 'center'
                        color: 'white'
                        pos_hint: {'center_x':0.5, 'center_y':0.92}
                        font_size: '25dp'
                        size_hint: 0.5, 0.5
                        padding: '10dp'
                MDCard:
                    style: 'elevated'
                    pos_hint: {'center_x':0.5, 'center_y':0.3}
                    md_bg_color: '#ffffff'
                    size_hint:1,1
                    radius: [0,100,0,0]
                    MDRelativeLayout:
                        MDLabel:
                            text: 'Name: Ashvin Dhakal'
                            halign: 'left'
                            bold: True
                            pos_hint: {'center_x':0.5, 'center_y':0.9}
                            size_hint_x:None
                            width:'400'
                            color: '#000000'
                            font_size: '18dp'
                        MDLabel:
                            text: "Username: @ashvin"
                            halign: 'left'
                            bold: True
                            pos_hint: {'center_x':0.5, 'center_y':0.85}
                            size_hint_x:None
                            width:'400'
                            color: '#000000'
                            font_size: '18dp'
                        MDLabel:
                            text: "Email: ashvindhakal111@gmail.com"
                            halign: 'left'
                            bold: True
                            pos_hint: {'center_x':0.5, 'center_y':0.8}
                            size_hint_x:None
                            width:'400'
                            color: '#000000'
                            font_size: '18dp'
                        ScrollView:
                            pos_hint: {'center_x':0.5, 'center_y':0.25}
                            MDList:
                                OneLineIconListItem:
                                    text: 'Settings'
                                    IconLeftWidget:
                                        icon: 'cog'
                                OneLineIconListItem:
                                    text: 'Uploads'
                                    IconLeftWidget:
                                        icon: 'file-upload'
                                OneLineIconListItem:
                                    text: 'Favourites'
                                    IconLeftWidget:
                                        icon: 'star'
                                OneLineIconListItem:
                                    text: 'Logout'
                                    IconLeftWidget:
                                        icon: 'logout'
                                

<MaleWorkouts>
    name: 'male_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_bg_color: 'Custom'
        md_bg_color: '#ffffff'
        size_hint_x: 1
        size_hint_y: 1
        radius: [0,0,0,0]
        MDCard:
            style: 'filled'
            pos_hint: {'center_x':0.5, 'center_y':0.45}
            size_hint_x: 1
            size_hint_y: 0.9
            theme_bg_color: 'Custom'
            md_bg_color: '#ffffff'
            radius: [0,0,0,0]
            GridLayout: 
                cols: 3
                padding: '10dp'
                spacing: '10dp'
                adaptive_height : True
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_abs_card_press("male_abs_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/abs_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Abs"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                               
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_leg_card_press("male_leg_workouts")
                    BoxLayout: 
                        orientation: 'vertical'
                        padding: '10dp'                       
                        FitImage: 
                            source: "Images/leg_male.jpg"
                            size_hint_y: 0.6
                            pos_hint: {'center_x':0.5,'center_y':0.65}
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text:'Leg'
                                color:'#ffffff'
                                bold: True
                                font_style: 'H6'
                                pos_hint: {'center_y':0.2}
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_chest_card_press("male_chest_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/chest_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Chest"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_shoulder_card_press("male_shoulder_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/shoulder_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [7,7]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Shoulder"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                        
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_back_card_press("male_back_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/back_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Back"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                        
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_thigh_card_press("male_thigh_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/thigh_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Thigh"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                       
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_arms_card_press("male_arms_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/arms_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Arms"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                       
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_biceps_card_press("male_biceps_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/biceps_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Biceps"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                        
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_male_neck_card_press("male_neck_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/neck_male.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Neck"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'mainscreen'    
    
    
<FemaleWorkouts>
    name: 'female_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_bg_color: 'Custom'
        md_bg_color: '#ffffff'
        size_hint_x: 1
        size_hint_y: 1
        radius: [0,0,0,0]
        MDCard:
            style: 'filled'
            pos_hint: {'center_x':0.5, 'center_y':0.45}
            size_hint_x: 1
            size_hint_y: 0.9
            theme_bg_color: 'Custom'
            md_bg_color: '#ffffff'
            radius: [0,0,0,0]
            GridLayout: 
                cols: 3
                padding: '10dp'
                spacing: '10dp'
                adaptive_height : True
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_abs_card_press("female_abs_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/abs_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Abs"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                               
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_leg_card_press("female_leg_workouts")
                    BoxLayout: 
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/leg_female.jpg"
                            size_hint_y: 0.6
                            pos_hint: {'center_x':0.5,'center_y':0.65}
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text:'Leg'
                                color:'#ffffff'
                                bold: True
                                font_style: 'H6'
                                pos_hint: {'center_y':0.2}
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_chest_card_press("female_chest_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/chest_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Chest"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_shoulder_card_press("female_shoulder_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/shoulder_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [7,7]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Shoulder"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                        
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_back_card_press("female_back_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/back_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Back"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                        
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_thigh_card_press("female_thigh_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/thigh_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Thigh"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                       
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_arms_card_press("female_arms_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/arms_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Arms"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                       
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_glutes_card_press("female_glutes_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/glutes_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Glutes"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}                        
                MDCard:
                    style: 'elevated'
                    theme_bg_color: 'Custom'
                    md_bg_color: '#000000'
                    size_hint_x: 0.9
                    size_hint_y: 0.1
                    radius: [10,10,10,10]
                    ripple_behavior: True  # Enables ripple effect to act like a button
                    on_release: root.on_female_neck_card_press("female_neck_workouts")
                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'
                        FitImage: 
                            source: "Images/neck_female.jpg"
                            pos_hint: {'center_x':0.5, 'center_y': 0.65}
                            size_hint_y: 0.6
                            radius: [10,10,10,10]
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: [10, 10]
                            size_hint_y: 0.3
                            MDLabel:
                                text: "Neck"
                                font_style: 'H6'
                                bold: True
                                color: '#ffffff'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        
        
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'mainscreen'
            
            
<MaleAbsWorkouts>
    name: 'male_abs_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        size_hint_x: 1
        size_hint_y: 0.9
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#ffffff'
        spacing: '10dp'
        BoxLayout:
            orientation: 'vertical'
            VideoPlayer:
                source: "Videos/male_abs_1.avi"
                allow_stretch: True
            VideoPlayer:
                id: video
                source: "Videos/male_abs_2.avi"
            VideoPlayer:
                id: video
                source: "Videos/male_abs_3.avi"
            
<MaleLegWorkouts>
    name: 'male_leg_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        size_hint_x: 1
        size_hint_y: 0.9
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#ffffff'
        spacing: '10dp'
        BoxLayout:
            orientation: 'vertical'
            VideoPlayer:
                source: "Videos/male_abs_1.avi"
                allow_stretch: True
            VideoPlayer:
                id: video
                source: "Videos/male_abs_2.avi"
            VideoPlayer:
                id: video
                source: "Videos/male_abs_3.avi"
            
<MaleChestWorkouts>
    name: 'male_chest_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
    MDLabel:
        text: 'Male Chest Exercises'
        halign: 'center'
            
<MaleShoulderWorkouts>
    name: 'male_shoulder_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
<MaleBackWorkouts>
    name: 'male_back_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
<MaleThighWorkouts>
    name: 'male_thigh_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
<MaleArmsWorkouts>
    name: 'male_arms_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
<MaleBicepsWorkouts>
    name: 'male_biceps_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
<MaleNeckWorkouts>
    name: 'male_neck_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'male_workouts'
        
            
<FemaleAbsWorkouts>
    name: 'female_abs_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        size_hint_x: 1
        size_hint_y: 0.9
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#ffffff'
        spacing: '10dp'
        BoxLayout:
            orientation: 'vertical'
            VideoPlayer:
                source: "Videos/female_abs_1.mp4"
                allow_stretch: True
            VideoPlayer:
                id: video
                source: "Videos/female_abs_2.mp4"
            VideoPlayer:
                id: video
                source: "Videos/female_abs_3.mp4"
        
<FemaleLegWorkouts>
    name: 'female_leg_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
    MDLabel:
        text: 'Female Leg Exercises'
        halign: 'center'
        
<FemaleChestWorkouts>
    name: 'female_chest_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
    MDLabel:
        text: 'Female chest Exercises'
        halign: 'center'
        
<FemaleShoulderWorkouts>
    name: 'female_shoulder_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
<FemaleBackWorkouts>
    name: 'female_back_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
<FemaleThighWorkouts>
    name: 'female_thigh_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
<FemaleArmsWorkouts>
    name: 'female_arms_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
<FemaleGlutesWorkouts>
    name: 'female_glutes_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
<FemaleNeckWorkouts>
    name: 'female_neck_workouts'
    MDCard:
        style: 'filled'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        size_hint_x: 1
        size_hint_y: 0.1
        radius: [0,0,0,0]
        theme_bg_color: 'Custom'
        md_bg_color: '#000000'
        padding: '10dp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_y':0.5}
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            on_press: root.manager.current = 'female_workouts'
"""


class MainScreen(Screen):
    def on_male_card_press(self, screen_name):
        # Set transition effect
        self.manager.transition = SlideTransition(duration=0.01)
        # Switch to the specified screen
        self.manager.current = screen_name
        print("Male card Pressed")

    def on_female_card_press(self, screen_name):
        # Set transition effect
        self.manager.transition = SlideTransition(duration=0.01)
        # Switch to the specified screen
        self.manager.current = screen_name

        print("Female card Pressed")


class MaleWorkouts(Screen):
    def on_male_abs_card_press(self, screen_name):
        print("Male abs card pressed.")
        self.manager.current = screen_name

    def on_male_leg_card_press(self, screen_name):
        print("Male leg card pressed.")
        self.manager.current = screen_name

    def on_male_chest_card_press(self, screen_name):
        print("Male chest card pressed.")
        self.manager.current = screen_name

    def on_male_shoulder_card_press(self, screen_name):
        print("Male shoulder card pressed.")
        self.manager.current = screen_name

    def on_male_back_card_press(self, screen_name):
        print("Male back card pressed.")
        self.manager.current = screen_name

    def on_male_thigh_card_press(self, screen_name):
        print("Male thigh card pressed.")
        self.manager.current = screen_name

    def on_male_arms_card_press(self, screen_name):
        print("Male arms card pressed.")
        self.manager.current = screen_name

    def on_male_biceps_card_press(self, screen_name):
        print("Male biceps card pressed.")
        self.manager.current = screen_name

    def on_male_neck_card_press(self, screen_name):
        print("Male neck card pressed.")
        self.manager.current = screen_name


class FemaleWorkouts(Screen):
    def on_female_abs_card_press(self, screen_name):
        print("Female abs card pressed.")
        self.manager.current = screen_name

    def on_female_leg_card_press(self, screen_name):
        print("Female leg card pressed.")
        self.manager.current = screen_name

    def on_female_chest_card_press(self, screen_name):
        print("Female chest card pressed.")
        self.manager.current = screen_name

    def on_female_shoulder_card_press(self, screen_name):
        print("Female shoulder card pressed.")
        self.manager.current = screen_name

    def on_female_back_card_press(self, screen_name):
        print("Female back card pressed.")
        self.manager.current = screen_name

    def on_female_thigh_card_press(self, screen_name):
        print("Female thigh card pressed.")
        self.manager.current = screen_name

    def on_female_arms_card_press(self, screen_name):
        print("Female arms card pressed.")
        self.manager.current = screen_name

    def on_female_glutes_card_press(self, screen_name):
        print("Female glutes card pressed.")
        self.manager.current = screen_name

    def on_female_neck_card_press(self, screen_name):
        print("Female neck card pressed.")
        self.manager.current = screen_name


class MaleAbsWorkouts(Screen):
    pass


class MaleLegWorkouts(Screen):
    pass


class MaleChestWorkouts(Screen):
    pass


class MaleShoulderWorkouts(Screen):
    pass


class MaleBackWorkouts(Screen):
    pass


class MaleThighWorkouts(Screen):
    pass


class MaleArmsWorkouts(Screen):
    pass


class MaleBicepsWorkouts(Screen):
    pass


class MaleNeckWorkouts(Screen):
    pass


class FemaleAbsWorkouts(Screen):
    pass


class FemaleLegWorkouts(Screen):
    pass


class FemaleChestWorkouts(Screen):
    pass


class FemaleShoulderWorkouts(Screen):
    pass


class FemaleBackWorkouts(Screen):
    pass


class FemaleThighWorkouts(Screen):
    pass


class FemaleArmsWorkouts(Screen):
    pass


class FemaleGlutesWorkouts(Screen):
    pass


class FemaleNeckWorkouts(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(MaleWorkouts(name='male_workouts'))
sm.add_widget(FemaleWorkouts(name='female_workouts'))
sm.add_widget(MaleAbsWorkouts(name='male_abs_workouts'))
sm.add_widget(MaleLegWorkouts(name='male_leg_workouts'))
sm.add_widget(MaleChestWorkouts(name='male_chest_workouts'))
sm.add_widget(MaleShoulderWorkouts(name='male_chest_workouts'))
sm.add_widget(MaleBackWorkouts(name='male_shoulder_workouts'))
sm.add_widget(MaleThighWorkouts(name='male_back_workouts'))
sm.add_widget(MaleArmsWorkouts(name='male_thigh_workouts'))
sm.add_widget(MaleBicepsWorkouts(name='male_arms_workouts'))
sm.add_widget(MaleNeckWorkouts(name='male_biceps_workouts'))
sm.add_widget(FemaleAbsWorkouts(name='female_neck_workouts'))
sm.add_widget(FemaleLegWorkouts(name='female_neck_workouts'))
sm.add_widget(FemaleChestWorkouts(name='female_neck_workouts'))
sm.add_widget(FemaleShoulderWorkouts(name='female_neck_workouts'))
sm.add_widget(FemaleBackWorkouts(name='female_neck_workouts'))
sm.add_widget(FemaleThighWorkouts(name='female_neck_workouts'))
sm.add_widget(FemaleArmsWorkouts(name='female_neck_workouts'))
sm.add_widget(FemaleGlutesWorkouts(name='female_glutes_workouts'))
sm.add_widget(FemaleNeckWorkouts(name='female_neck_workouts'))


class HomeScreenApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(KV)
        return screen


if __name__ == '__main__':
    HomeScreenApp().run()
