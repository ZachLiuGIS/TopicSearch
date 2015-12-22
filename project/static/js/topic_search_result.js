$(function() {

	var update_topic_likes = function() {
		var api_url = '/topic_search/api/search_topic_likes/';
		var topic = $('#id_search_topic').text();
		console.log(topic);

		$.ajax(api_url, {
			dataType: 'json',
			data: {name: topic},
			method: 'POST'
		}).done(function(data) {
			console.log(data);
			$('#id_btn_like_topic').prop('disabled', true);
			$('#id_num_of_likes').text(parseInt($('#id_num_of_likes').text()) + 1)
		});
	};

	var bindEvents = function() {
		$('#id_btn_like_topic').on("click", update_topic_likes);
	};


	var init = function() {
		bindEvents();
	};

	init();
});