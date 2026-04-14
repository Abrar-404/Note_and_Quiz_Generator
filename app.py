import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image


# title section 
st.title('Note Summary and Quiz Generator', anchor=False)
st.markdown('Upload upto 3 images to generate Note Summary and Quiz')
st.divider()

# sidebar section
with st.sidebar:
  
  # Image section
  images = st.file_uploader(
    "Upload the notes (images) here",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
  )
  
  pil_images = []
    
  for img in images:
    pil_img = Image.open(img)
    pil_images.append(pil_img)
  
  if images:
    if(len(images) > 3):
      st.error("Please upload a maximum of 3 images.")
    else:
      st.subheader("Uploaded Images:")
      
      cols = st.columns(len(images))
      
      for i, img in enumerate(images):
        with cols[i]:
          st.image(img)
          
  
  # difficulty section
  select_options = st.selectbox(
    "Select the difficulty level for the quiz:",
    ("Easy", "Medium", "Hard"), 
    index = None
  )

  button = st.button('Generate :streamlit:', use_container_width=True)
  

if button:
  if not images:
    st.error("Please upload at least one image.")
  if not select_options:
    st.error("Please select a difficulty level for the quiz.")
    
  if images and select_options:
    # note section
    with st.container(border=True):
      st.subheader('Your Notes')
      
      with st.spinner('Sit tight, we are generating your notes...'):
        notes = note_generator(pil_images)
        st.markdown(notes)
    
    # audio transcription section
    with st.container(border=True):
      st.subheader('Audio Transcription')
      
      with st.spinner('Sit tight, we are generating your audio...'):
        
        # Clearing the markdown audio
        notes = notes.replace('#', "")
        notes = notes.replace('*', "")
        notes = notes.replace('-', "")
        notes = notes.replace("", "")
        
        audio_transcript = audio_transcription(notes)
        st.audio(audio_transcript)
    
    # quiz section
    with st.container(border=True):
      st.subheader(f':question: Quiz ({select_options})')
      
      with st.spinner('Sit tight, we are generating your quiz...'):
        quizzes = quiz_generator(pil_images, select_options)
        st.markdown(quizzes)