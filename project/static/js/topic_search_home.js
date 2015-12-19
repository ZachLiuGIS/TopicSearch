$(function() {
	var checkboxIsChecked = function (selector) {
		return $(selector).prop('checked');
	};

	var updateGeoLocation = function() {
		if (checkboxIsChecked('#id_cb_geo_search')) {
			if (navigator.geolocation) {
				$('#id_btn_search_go').prop('disabled', true);

				// using geo location api to update lat and lng. button should be disabled before callback executed.
				navigator.geolocation.getCurrentPosition(function(location) {
					var lat = location.coords.latitude;
					var lng = location.coords.longitude;

					console.log(lat, lng);

					$('#id_input_lat').val(lat);
					$('#id_input_lng').val(lng);
					$('#id_btn_search_go').prop('disabled', false);
				});
			} else {
				// handle geolocation not supported.
				alert("Geolocation is not supported by this browser.");
				$('#id_cb_geo_search').attr('checked', false);
			}
		}
	}

	var bindEvents = function() {
		$('#id_cb_geo_search').on("click", updateGeoLocation);
	}

	var init = function() {
		bindEvents();
	}

	init();
});