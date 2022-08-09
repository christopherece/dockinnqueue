setTimeout(function(){
    $('#message').fadeOut('slow');
    console.log('Removing mesage')
},5000);

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

