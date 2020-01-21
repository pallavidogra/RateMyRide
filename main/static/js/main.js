var post_id = "";
$( document ).ready(function() {
  // Js for ratign module

    $('#stars li').on('mouseover', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
   
    // Now highlight all the stars that's not after the current hovered star
    $(this).parent().children('li.star').each(function(e){
      if (e < onStar) {
        $(this).addClass('hover');
      }
      else {
        $(this).removeClass('hover');
      }
    });
    
  }).on('mouseout', function(){
    $(this).parent().children('li.star').each(function(e){
      $(this).removeClass('hover');
    });
  });
  
  /* 2. Action to perform on click */
  $('#stars li').on('click', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently selected
    var stars = $(this).parent().children('li.star');
    $.ajax({
        url: 'add_rating/',  //update rating in database
        type: 'POST',
        data: {
          'rating':  onStar,
          'post_id': post_id
        },
        success: function (response) {
          // var stars = $(this).parent().children('li.star');
          for (i = 0; i < stars.length; i++) {
            $(stars[i]).removeClass('selected');
          }
          
          for (i = 0; i < onStar; i++) {
            $(stars[i]).addClass('selected');
          }
        }
      });
    // var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
  }); 
    $('.pop').on('click', function(e) {
    var image_id = $(this).find('img').attr('id');
    var post_title = "#post-title-" + image_id;
    var post_description = "#post-description-" + image_id;
    var post_date_posted = "#post-date-posted-" + image_id;
    var post_author = "#post-author-" + image_id;
    var post_text_title = $(post_title).text();
    var post_text_description = $(post_description).text();
    var post_text_date_posted = $(post_date_posted).text();
    var post_text_author = $(post_author).text();
    $('.imagepreview').attr('src', $(this).find('img').attr('src'));
    $('.post-title-p').text(post_text_title)
    $('.post-description-p').text(post_text_description)
    $('.post-date-posted-p').text(post_text_date_posted)
    $('.post-author-p').text(post_text_author)
    post_id = image_id; //post is define to update rating in database for above rating func
    $.ajax({
        url: 'get_rating/',  //get rating of every post modal from database
        type: 'POST',
        data: {
          'post_id': post_id
        },
        success: function (response) {
          var stars = $("#stars li");
          for (i = 0; i < stars.length; i++) {
            $(stars[i]).removeClass('selected');
          }
          
          for (i = 0; i < response.rating; i++) {
            $(stars[i]).addClass('selected');
          }
        }
    });
    $('#imagemodal').modal('show');
    openProfile = $(this);
  });


$('.pop').on('click', function(e) {
    var image_id = $(this).find('img').attr('id');
    var post_title = "#post-title-" + image_id;
    var post_description = "#post-description-" + image_id;
    var post_date_posted = "#post-date-posted-" + image_id;
    var post_author = "#post-author-" + image_id;
    var post_review = "#post-review-" + image_id;//rating functionality
    var post_text_title = $(post_title).text();
    var post_text_description = $(post_description).text();
    var post_text_date_posted = $(post_date_posted).text();
    var post_text_author = $(post_author).text();
    var post_get_review = $(post_review).text();//rating functionality
    $('.imagepreview').attr('src', $(this).find('img').attr('src'));
    $('.post-title-p').text(post_text_title);
    $('.post-description-p').text(post_text_description);
    $('.post-date-posted-p').text(post_text_date_posted);
    $('.post-author-p').text(post_text_author);
    $('#imagemodal').modal('show');

    openProfile = $(this);
    var cards = openProfile.parents('#gallery').find(".pop");
    var currentCardIndex = cards.index(openProfile);
    if(cards.length == currentCardIndex+1){
      $('.prev').show(); 
      $('.next').hide(); 
    }
    else if(currentCardIndex == 0){
      $('.prev').hide(); 
      $('.next').show();        
    } 
    else if(cards.length > (currentCardIndex + 1)) {
      $('.prev').show(); 
      $('.next').show();
    }
  }); 

  $(".next").click(function(event){
    var cards = openProfile.parents('#gallery').find(".pop");
    var currentCardIndex = cards.index(openProfile);
    if(cards.length > (currentCardIndex + 1)) { 
      cards.get(currentCardIndex + 1).click();        
      setTimeout(function() {
        $("#imagemodal").modal("show");
      },500);
    }
  });

  $(".prev").click(function(event){
    var cards = openProfile.parents('#gallery').find(".pop");
    var currentCardIndex = cards.index(openProfile);             
    if(currentCardIndex > 0) {         
      cards.get(currentCardIndex - 1).click();             
      setTimeout(function() {
        $("#imagemodal").modal("show");
      },500);        
    } 
  });
});