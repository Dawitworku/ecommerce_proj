// $('p').click(function () {
//     alert('Clicked me!')
// })
// Ajax request for the email field to update info on the fly
$('#email-ajax').keyup(function (event) {
    //console.log(event.target.value)
    if ((event.target.value).length == 0) { // Removing the email_ajax_error if the email field is empty.
        //console.log("changing the timer")
        $('#email_ajax_error').text('');
    } else {
        $.ajax({
            url: '/email_check',
            method: 'POST',
            data: {
                email: event.target.value, //instead of passing the whole form, we can pass just the email and generate a token on the spot
                csrfmiddlewaretoken: getCookie('csrftoken'), // generating a token for our csrf since we are not passing out the form that has the csrf token included
            },
            success: function (response) {
                //console.log(response);
                $('#email_ajax_error').html(response);
            }
        })
    }
})
// Setting timeout for the alert error messages.
setTimeout(function () {
    $('.alert').fadeOut(3500);

}, 4000);



// Function that generates and matches the csrf token generated while submitting the form.
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}