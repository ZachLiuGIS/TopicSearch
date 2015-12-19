$(function() {
	var checkboxIsChecked = function (selector) {
		return $(selector).prop('checked');
	};

	var display_searching = function() {
		$('#id_search_loader').show();
	};

	var updateGeoLocation = function() {
		if (checkboxIsChecked('#id_cb_geo_search')) {
			if (navigator.geolocation) {
				// temporarily disable search button and display progress until location updated.
				$('#id_btn_search_go').prop('disabled', true);
				$('#id_form_message_muted').text('Updating search location...');

				// using geo location api to update lat and lng. button should be disabled before callback executed.
				navigator.geolocation.getCurrentPosition(function(location) {
					var lat = location.coords.latitude;
					var lng = location.coords.longitude;

					console.log(lat, lng);

					$('#id_input_lat').val(lat);
					$('#id_input_lng').val(lng);
					$('#id_btn_search_go').prop('disabled', false);
					$('#id_form_message_muted').text('');
				});
			} else {
				// handle geolocation not supported.
				alert("Geolocation is not supported by this browser.");
				$('#id_cb_geo_search').attr('checked', false);
			}
		}
	};

	var onSearchClick = function() {
		display_searching();
	};

	var display_word_cloud = function(data) {
		data = data.map(function(item) {
			item.text = item.text.replace("#", "");
			return $.extend(item, {link: 'topic_search/search_result/?term=' + item.text})
		});

		$("#id_topic_trends").jQCloud(data, {
		  width: 600,
		  height: 200
		});
	};

	var load_trend_topics = function() {
		var api_url = 'topic_search/api/twitter_trends/?format=json';
		$.ajax(api_url, {
			dataType: 'json'
		}).done(function(data) {
		console.log(data);

			if (data == "API Search Error") {
				$('#id_trend_message_error').text('Something wrong with loading trending topics, but you can still search');
			} else {
				display_word_cloud(data);
			}
			$('#id_trends_loader').hide();
		})
	};



	var bindEvents = function() {
		$('#id_cb_geo_search').on("click", updateGeoLocation);
		$('#id_btn_search_go').on("click", onSearchClick);
		$('#id_topic_trends').on("click", "a", display_searching);
	};


	var init = function() {
		bindEvents();
		load_trend_topics();
		$('#id_search_loader').hide();
	};

	init();
});