from django.shortcuts import render
from django.conf import settings
from langchain_groq import ChatGroq

def story(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        if topic:
            llm = ChatGroq(
                groq_api_key=settings.GROQ_API_KEY,
                model_name="llama-3.1-70b-versatile"
            )
            
            prompt = """
            You are a content writer. Write engaging and SEO-friendly content based on the topic provided.
            Format the content with proper HTML tags:
            - Use <h2> for headings (without asterisks)
            - Use <p> for paragraphs
            - Add proper spacing between sections
            
            Topic: {topic}
            """
            
            response = llm.invoke(prompt.format(topic=topic))
            
            # Clean up any remaining asterisks
            content = response.content.replace('**', '')
            
            return render(request, 'contentapp/generate.html', {
                'content': content,
                'topic': topic
            })
    
    return render(request, 'contentapp/generate.html') 
