/* 
* @Author: cnicolas
* @Date:   2015-10-20 14:43:50
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-13 15:41:34
*/

'use strict';

$(document).ready(function() {
	// Init the mobile navbar
	$(".button-collapse").sideNav();
	// Init the parallax
	$('.parallax').parallax();
	// Init the modals
	$(".modal-trigger").leanModal();
	$("#modal-connection").closeModal();

	// Show toasts
	$("span.error-toast").each(function(ind, val) {
		Materialize.toast(this.innerHTML, 4000, "red");
	});
	$("span.success-toast").each(function(ind, val) {
		Materialize.toast(this.innerHTML, 4000, "light-green");
	});
});