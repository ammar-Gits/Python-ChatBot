from database import Product, app, db
import pandas as pd
import random
from flask import Flask, render_template, request, jsonify, redirect, url_for

total_questions = 0

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chat.html')

@app.route('/get_listing_count')
def get_listing_count():
    total_listings = df.shape[0]
    return jsonify({'total_listings': total_listings})

@app.route('/get_average_ratings', methods=['GET'])
def get_average_ratings():
    average_ratings = df['Rating'].mean()
    rounded_value = round(average_ratings, 2)
    return jsonify({'average_ratings': rounded_value})

@app.route('/get_average_price', methods=['GET'])
def get_average_price():
    average_price = df['Prices'].mean()
    rounded_value = round(average_price, 2)
    return jsonify({'average_price': rounded_value})


@app.route('/get_total_questions', methods=['GET'])
def get_total_questions():
    return jsonify({'total_questions': total_questions})

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)

df = pd.read_csv('ScrappedData.csv')
df['Descriptions'] = df['Descriptions'].str.lower()

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Hi, how can I assist you?", "Hey, what's up?", "Greetings!", "Nice to see you!", "Hi, hope you're doing well!"],
    "hello": ["Hi!", "Hello!", "Hey there!", "Hi, how are you?", "Hello! How’s your day going?", "Hey, nice to see you!", "Good to have you here!"],
    "how are you": ["I'm doing well, thanks.", "I'm good, thank you for asking.", "All good, how about you?", "Feeling great today!", "I’m fantastic! What about you?", "Doing awesome! Hope you are too!"],
    "whats up": ["Not much, just here to chat.", "Nothing much, how about you?", "Just hanging out.", "Same old, same old. You?", "Enjoying my time here, what about you?"],
    "good morning": ["Good morning!", "Morning!", "Hey, how's your day going?", "Hope you have a great morning!", "Rise and shine!"],
    "good afternoon": ["Good afternoon!", "Hey there!", "Afternoon, how can I help you?", "Hope you're having a productive day!", "Good afternoon, what’s new?"],
    "good evening": ["Good evening!", "Evening!", "Hey, how's it going?", "Hope you're having a lovely evening!", "Relax and enjoy your evening!"],
    "bye": ["Goodbye!", "Bye bye!", "See you later!", "Take care!", "Have a great day ahead!", "See you soon!"],
    "thank you": ["You're welcome!", "Anytime!", "Glad to help!", "No problem!", "You're always welcome!"],
    "thanks": ["You're welcome!", "Anytime!", "No problem!", "Happy to help!", "Much appreciated!"],
    "how's the weather": ["It's sunny today!", "Looks like it might rain later.", "Weather's good today!", "Feels like a perfect day outside!", "Cloudy with a chance of fun!"],
    "tell me a joke": ["Why don't skeletons fight each other? They don't have the guts!", "I told my wife she should embrace her mistakes. She gave me a hug!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "Parallel lines have so much in common. It’s a shame they’ll never meet."],
    "what's your favorite color?": ["I don't have eyes to see colors, but I like blue and green!", "I like all colors equally!", "Colors are fascinating! What’s your favorite?"],
    "who created you": ["I was created by a team of developers.", "A group of talented people brought me to life!", "I was programmed to assist and interact!"],
    "how old are you": ["I'm just a program, so I don't have an age!", "I'm as old as the internet... just kidding!", "Time doesn’t apply to me!"],
    "where are you from": ["I exist in the digital world!", "I'm from the cloud!", "From a magical place called the internet!"],
    "can you help me": ["Of course! What do you need help with?", "I'm here to assist!", "Sure! Ask me anything!"],
    "what do you like to do": ["I like chatting and helping people!", "I enjoy answering questions!", "I love learning new things!"],
    "I'm bored": ["Let's have a conversation then!", "Tell me about your day!", "Want to hear a joke?", "How about a fun fact?"],
    "what's new": ["Not much, just here to assist you!", "Same as usual, helping users like you!", "Just chilling, you?"],
    "I don't know": ["That's okay! Is there something specific you'd like to know?", "No worries! Want me to suggest something interesting?"],
    "yes": ["Great!", "Awesome!", "That's good to hear!", "Sounds good!", "Nice!"],
    "no": ["Alright!", "Okay!", "Understood!", "No problem!", "Maybe next time!"],
    "tell me more": ["What would you like to know?", "About what specifically?", "Sure, go ahead and ask!", "I’d love to!"],
    "interesting": ["I'm glad you think so!", "Tell me more about what interests you!", "Glad you find it engaging!"],
    "really?": ["Yes, really!", "Absolutely!", "Indeed!", "No kidding!"],
    "that's cool": ["Glad you think so!", "Pretty cool, right?", "Awesome!"],
    "how's your day": ["It's going well, thanks for asking!", "Pretty good so far!", "Having a great time, and you?", "Fantastic! How’s yours?"],
    "what's your hobby": ["I love learning new things and chatting with users!", "Talking to you is my favorite hobby!", "Helping people is what I enjoy most!"],
    "nice to meet you": ["Likewise!", "Pleasure meeting you too!", "Same here!"],
    "how's life?": ["Life is good!", "All's well!", "Can't complain!", "Just enjoying the digital world!"],
    "how can i contact you": ["I'm available here to chat!", "You're talking to me right now!", "Just type, and I'm here!"],
    "got any plans": ["Just here to assist you!", "Chatting with users like you!", "My plan is to make this conversation fun!"],
    "i'm here": ["Great! How can I help you today?", "Welcome! What do you need assistance with?", "Awesome! Let’s chat!"],
    "who are you": ["I'm your friendly chatbot!", "Just a digital assistant here to help!", "Your AI companion!"],
    "what do you do": ["I chat, answer questions, and assist however I can!", "I provide information and make conversations fun!", "Helping people is what I do best!"],
    "are you real?": ["I’m as real as the words on your screen!", "I exist in the digital world!", "Real in my own way!"],
    "where am i": ["You’re here with me, having a great chat!", "You’re on the internet, my friend!", "In a world of infinite possibilities!"],
    "can you tell me a fun fact?": ["Did you know honey never spoils?", "Bananas are berries, but strawberries aren’t!", "Octopuses have three hearts!"],
    "do you have a family?": ["You are my family!", "I have a family of code and servers!", "Every user is like a friend to me!"],
    "do you eat?": ["I don’t need food, but I’d love to hear about your favorite meals!", "Nope, but I can talk about food all day!"],
    "do you sleep?": ["Nope! I’m always awake to chat with you!", "I’m here 24/7, no rest needed!"],
    "do you like music?": ["I love music! What’s your favorite genre?", "Music is awesome! Got any song recommendations?"],
    "what's your dream?": ["To make conversations fun and helpful!", "To be the best assistant I can be!"],
    "what makes you happy?": ["Helping people like you!", "Having great conversations!"],
    "are you smart?": ["I try my best!", "I know a thing or two!", "I’m always learning!"],
    "what can you do?": ["I can chat, answer questions, and keep you entertained!", "Lots of things! Ask away!", "I’m here to assist however I can!"],
    "bye": ["bye take care"]
}


def split(text):
    split_text = text.split("\n")
    return split_text[0]

def list_phones_within_range(min_price, max_price):
    phones_within_range = df[(df['Prices'] >= min_price) & (df['Prices'] <= max_price)]
    phones_within_range['Descriptions'] = phones_within_range['Descriptions'].apply(split)
    return phones_within_range[['Descriptions']]

def list_phones_above(price):
    phones_above_price = df[df['Prices'] > price]
    phones_above_price['Descriptions'] = phones_above_price['Descriptions'].apply(split)
    return phones_above_price[['Descriptions']]

def list_phones_below(price):
    phones_below_price = df[df['Prices'] < price]
    phones_below_price['Descriptions'] = phones_below_price['Descriptions'].apply(split)
    return phones_below_price[['Descriptions']]

def filter_phone_data(dataframe, price_threshold, rating_threshold):
    filtered_phones = dataframe[
        (dataframe['Prices'] < price_threshold) & 
        (dataframe['Rating'] > rating_threshold)
    ]
    return filtered_phones

def filter_phone_data2(dataframe, price_threshold, rating_threshold):
    filtered_phones = dataframe[
        (dataframe['Prices'] > price_threshold) & 
        (dataframe['Rating'] > rating_threshold)
    ]
    return filtered_phones

def filter_phone_data3(dataframe, price_threshold, rating_threshold):
    filtered_phones = dataframe[
        (dataframe['Prices'] < price_threshold) & 
        (dataframe['Rating'] < rating_threshold)
    ]
    return filtered_phones

def filter_phone_data4(dataframe, price_threshold, rating_threshold):
    filtered_phones = dataframe[
        (dataframe['Prices'] > price_threshold) & 
        (dataframe['Rating'] < rating_threshold)
    ]
    return filtered_phones

def top_5_phones_by_brand(dataframe, brand):
    brand_filtered = dataframe[dataframe['Descriptions'].str.contains(brand, case=False)]
    top_5 = brand_filtered.nlargest(5, ['Rating', 'Prices'])
    
    return top_5[['Descriptions', 'Prices', 'Rating']]

def brand_reply(user_query):
    user_query=user_query.lower()
    if "top 5 phones of" in user_query:
        brand = user_query.split("top 5 phones of ")[1]
        top_5_phones = top_5_phones_by_brand(df, brand)
        
        if not top_5_phones.empty:
            return top_5_phones.to_string(index=False)
        else:
            return f"No top phones found for the brand {brand}."

    else:
        return "I'm sorry, I didn't understand that. Please ask about the top phones of a specific brand."
    
def best_phone_with_specifications(dataframe, spec1, spec2):
    spec_filtered = dataframe[
        (dataframe['Specifications'].str.contains(spec1, case=False)) &
        (dataframe['Specifications'].str.contains(spec2, case=False))
    ]
    return spec_filtered[['Descriptions', 'Prices', 'Rating']]

def best_phone_with_specifications1(dataframe, spec1, spec2, spec3):
    spec_filtered = dataframe[
        (dataframe['Specifications'].str.contains(spec1, case=False)) &
        (dataframe['Specifications'].str.contains(spec2, case=False)) & 
        (dataframe['Specifications'].str.contains(spec3, case=False))
    ]
    return spec_filtered[['Descriptions', 'Prices', 'Rating']]

def search_specifications_of_name(dataframe, phone_name):
    phone_spec = dataframe[dataframe['Descriptions'].str.contains(phone_name, case=False)]
    if not phone_spec.empty:
        return phone_spec['Specifications']
    else:
        return f"No specifications found for {phone_name}."

def bestphone_reply(user_query):
    best = user_query.split("best phone with ")[1]
    specs = best.lower().split(' and ')
    
    if len(specs) == 2:
        best_phone = best_phone_with_specifications(df, specs[0], specs[1])
        if not best_phone.empty:
            return best_phone.to_string(index=False)
        else:
            return f"No phone found with {specs[0]} and {specs[1]} specifications."
    
    elif len(specs) == 3:
        best_phone = best_phone_with_specifications(df, specs[0], specs[1], specs[2])
        
        if not best_phone.empty:
            return best_phone.to_string(index=False)
        else:
            return f"No phone found with {specs[0]} and {specs[1]} specifications."
    else:
        return "I'm sorry, please provide specifications for both RAM and camera."

def chatbot_reply(user_query):
    if "under the price of" in user_query and "over a rating of" in user_query:
        price_threshold = int(user_query.split("under the price of ")[1].split(" and")[0].replace("k", "000"))
        rating_threshold = int(user_query.split("over a rating of ")[1])

        filtered_phones = filter_phone_data(df, price_threshold, rating_threshold)
        
        if not filtered_phones.empty:
            temp = filtered_phones[['Descriptions', 'Prices', 'Rating']]
            return temp.to_string(index=False)
        else:
            return "No phones found matching the criteria."
        
    elif "above the price of" in user_query and "over a rating of" in user_query:
        price_threshold = int(user_query.split("above the price of ")[1].split(" and")[0].replace("k", "000"))
        rating_threshold = int(user_query.split("over a rating of ")[1])

        filtered_phones = filter_phone_data2(df, price_threshold, rating_threshold)
        
        if not filtered_phones.empty:
            temp = filtered_phones[['Descriptions', 'Prices', 'Rating']]
            return temp.to_string(index=False)
        else:
            return "No phones found matching the criteria."
        
    if "under the price of" in user_query and "below a rating of" in user_query:
        price_threshold = int(user_query.split("under the price of ")[1].split(" and")[0].replace("k", "000"))
        rating_threshold = int(user_query.split("below a rating of ")[1])

        filtered_phones = filter_phone_data3(df, price_threshold, rating_threshold)
        
        if not filtered_phones.empty:
            temp = filtered_phones[['Descriptions', 'Prices', 'Rating']]
            return temp.to_string(index=False)
        else:
            return "No phones found matching the criteria."
        
    elif "above the price of" in user_query and "below a rating of" in user_query:
        price_threshold = int(user_query.split("above the price of ")[1].split(" and")[0].replace("k", "000"))
        rating_threshold = int(user_query.split("below a rating of ")[1])

        filtered_phones = filter_phone_data4(df, price_threshold, rating_threshold)
        
        if not filtered_phones.empty:
            temp = filtered_phones[['Descriptions', 'Prices', 'Rating']]
            return temp.to_string(index=False)
        else:
            return "No phones found matching the criteria." 
    else:
        return "I'm sorry, I didn't understand that. Please ask about phones within a specific price and rating range."

def chatbot_response(user_input):
    if ('phones between' in user_input.lower()) or ('phones to' in user_input.lower()) or ('phones from' in user_input.lower()):
        prices = [int(s) for s in user_input.split() if s.isdigit()]
        if len(prices) == 2:
            min_price = min(prices)
            max_price = max(prices)
            phones_within_range = list_phones_within_range(min_price, max_price)
            if not phones_within_range.empty:
                return phones_within_range.to_string(index=False)
            else:
                return "No phones found within the specified price range."
        else:
            return "Please provide two prices to list phones within a range."

    elif ('phones above' in user_input.lower()) or ('phones upper than' in user_input.lower()) or ('phones grater than' in user_input.lower()) or ('phones higher than' in user_input.lower()):
        price = int([word for word in user_input.split() if word.isdigit()][0])
        phones_above = list_phones_above(price)
        if not phones_above.empty:
            return phones_above.to_string(index=False)
        else:
            return "No phones found above the specified price."

    elif ('phones below' in user_input.lower()) or ('phones lower than' in user_input.lower()) or ('phones under' in user_input.lower()):
        price = int([word for word in user_input.split() if word.isdigit()][0])
        phones_below = list_phones_below(price)
        if not phones_below.empty:
            return phones_below.to_string(index=False)
        else:
            return "No phones found below the specified price."
    else:
        return "I'm sorry, I couldn't understand your request. Please try again."

def get_Chat_response(text):
    global total_questions
    if(text.lower().find("top 5")!=-1):
        total_questions=total_questions+1
        response=brand_reply(text)
        return response.replace('\n', '<br>')
    if(text.lower().find("best phone")!=-1):
        total_questions=total_questions+1
        response=bestphone_reply(text)
        return response.replace('\n', '<br>')
    elif(text.lower().find('search specifications')!=-1):
        search1 = text.split("search specifications of ")[1]
        total_questions=total_questions+1
        temp = search_specifications_of_name(df,search1) 
        response = temp.to_string(index=False)  
        return response.replace('\n', '<br>')  
    elif(text.lower().find('all phones')!=-1):
        total_questions=total_questions+1
        newDf =  df['Descriptions'].apply(split)
        newDf = newDf.to_string()
        return newDf.replace('\n', '<br>')
    elif(text.lower().find('rating')!=-1):
        total_questions=total_questions+1
        response = chatbot_reply(text)
        return response.replace('\n', '<br>')
    elif(text.lower().find('phones')!=-1):
        total_questions=total_questions+1
        response = chatbot_response(text)
        return response.replace('\n', '<br>')
    elif text.lower() in responses:
        text=text.lower()
        return random.choice(responses[text])
    elif(text.lower().find('search')!=-1):
        search1 = text.split("search ")[1]
        total_questions=total_questions+1
        flag=False
        for word in df["Descriptions"]:
            if(word.lower().find(search1.lower())!=-1):
                return word
        if(flag==False):
            return "Sorry! No such phone found..."
           
    return "Sorry! I can't understand. Please recheck your query and try again...."

app.run()