// Function used to shrink nav bar removing paddings and adding black background 
$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('.nav').addClass('affix');
        console.log("OK");
    } else {
        $('.nav').removeClass('affix');
    }
});

$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

// Ajax function for filtering based on Categories and gender

$('.nav-link').click(function(event) {
    event.preventDefault();
    var cat_id = $(this).attr('category_id');
    // var prod_type = $(this).attr('prod_type');
    console.log(cat_id);
    // console.log(prod_type);

    $.ajax({
        url: `/show_category/${cat_id}`,
        method: 'GET',
        success: function(response) {
            console.log(response)
            $('#partial_render').html(response)
        }
    })
})
// Ajax call for ALL products under catagories
$('#all_cat').click(function(event) {
    event.preventDefault();
    var cat = $(this).attr('cat_all')
    console.log(cat)

    $.ajax({
        url: `/show_category/${cat}`,
        method: 'GET',
        success: function (response) {
            console.log(response)
            $('#partial_render').html(response)
        }
    })
})
// // Adding mouse over effect on the LOGOUT button
// $('#logout-color').mouseover(function(){ 
//     $(this).css('color', 'red');
// }).mouseout(function(){
//     $(this).css('color', 'white');
// });

$('#to_cart_form').submit(function (event) {
    event.preventDefault();
    var form = $(this)
    var id = $(this).attr('prod_id');
    console.log(form.serialize())
    console.log(id)
    // console.log({{request.session.user_id}})
    $.ajax({
        url: `/add_cart/${id}`,
        method: 'POST',
        data: form.serialize(),
        success: function (response) {
            console.log(response)
            if (response == "fail!") {
                // location.href="/login" // This is redirecting to my log and reg page if my user is not in sessions or logged in.
            console.log('temp')
            }
        }
    })

})



