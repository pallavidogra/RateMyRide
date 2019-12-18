$( document ).ready(function() {
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
		$('#imagemodal').modal('show');
		currentProfile = $(this);

	});
	$(".next").click(function(event){
      var posts = currentProfile.parents('.gallery').find(".pop");
      console.log('posts',posts)
      var currentPostIndex = posts.index(currentProfile);
      if(posts.length > (currentPostIndex + 1)) {
        posts.get(currentPostIndex + 1).click();
        setTimeout(function() {
          $("#imagemodal").modal("show");
        },500);
      } else {
        alert("You are on the last card!");
      }
    });
    
    $(".prev").click(function(event){
      var posts = currentProfile.parents('.gallery').find(".pop");
      console.log('posts',posts)
      var currentPostIndex = posts.index(currentProfile);
      if(currentPostIndex > 0) {
        posts.get(currentPostIndex - 1).click();
        setTimeout(function() {
          $("#imagemodal").modal("show");
        },500);
      } else {
        alert("You are on the first card!");
      }
      
    });
}); 
