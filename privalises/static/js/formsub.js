const usernames1 = document.getElementById('id_username')
const imgBox = document.getElementById('imgbox')
const email = document.getElementById('id_email')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const form = document.getElementById('forms')
const image = document.getElementById('id_image')
const url = ""

image.addEventListener('change', ()=>{
      const img_data = image.files[0]
      const url = URL.createObjectURL(img_data)
      imgBox.innerHTML = '<img src="${url}" width="100%">'


})



