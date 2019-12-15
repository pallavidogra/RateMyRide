$( document ).ready(function() {
	$(function() {
		var selectedClass = "";
		$(".filter").click(function(){
			selectedClass = $(this).attr("data-rel");
			$("#gallery").fadeTo(100, 0.1);
			$("#gallery div").not("."+selectedClass).fadeOut().removeClass('animation');
			setTimeout(function() {
			$("."+selectedClass).fadeIn().addClass('animation');
			$("#gallery").fadeTo(300, 1);
			}, 300);
		});
	});
    
    $(function() {
    	$('.pop').on('click', function() {
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
			$('.icon').addClass('glyphicon glyphicon-chevron-right');
			$('.icon').css('margin-top','55px');
			$('.icon').css('float','right');
			$('.icon').css('font-size','30px');
			$('.icon-left').addClass('glyphicon glyphicon-chevron-left');
			$('.icon-left').css('margin-top','215px');
			$('.icon-left').css('font-size','30px');			
		})
    }); 

});

