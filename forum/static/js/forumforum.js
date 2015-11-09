/* 
* @Author: cnicolas
* @Date:   2015-11-06 16:48:24
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-06 16:50:18
*/

'use strict';

$(document).ready(function() {
	setTimeout(function() {
		var toExpand = window.location.href.substr(window.location.href.indexOf('#'), window.location.href.length);
		var jvar = $(toExpand);
		jvar.parent().parent().parent().prev().click()
		setTimeout(function() {
			jvar.click();
		}, 100);
	}, 100);
});