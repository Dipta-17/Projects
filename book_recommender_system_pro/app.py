from flask import Flask,render_template,request, redirect, url_for
import pickle
import numpy as np

popular_df=pickle.load(open('popular.pkl','rb'))

pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similarity_scores=pickle.load(open('similarity_scores.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=[round(r, 1) for r in popular_df['avg_rating'].values],
                        #    rating=list(popular_df['avg_rating'].values), 
                           
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/contact')
def contact_ui():
    return render_template('contact.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    feedback = request.form.get('feedback')
    suggestions = request.form.get('suggestions')
    
    # You can save the feedback to a database or file here if needed.
    
    # Render a thank-you page with the user's name.
    return render_template('thanku.html', name=name)

@app.route('/recommend_books',methods=['POST'])
def recommend():
    user_input=request.form.get('user_input')

    if user_input == '':
        return render_template('recommend.html', error_message="Please enter a book name!")
    
    # Check if the book exists in the 'pt' index (which represents available books)
    if user_input not in pt.index:
        return render_template('recommend.html', error_message="Sorry, the book information is not available at this time.")
    
    index=np.where(pt.index== user_input)[0][0]
    
    similar_items=sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]

    data=[]
    for i in similar_items:
        item=[]
        #print(pt.index[i[0]])
        temp_df=books[books['Book-Title']==pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    
    if not data:
        return render_template('recommend.html', error_message="Sorry, the book information is not available at this time.")


    #print(data)    
    return render_template('recommend.html',data=data)


if __name__=='__main__':
    app.run(debug=True)