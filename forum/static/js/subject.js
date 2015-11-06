/* 
* @Author: cnicolas
* @Date:   2015-11-04 11:59:14
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-04 12:07:46
*/

'use strict';

$(document).ready(function() {
	$('button#answer').click(function() {
		$(this).addClass('hidden');
		$('section#section_answer').removeClass('hidden');
	});
	$('button#answer_hide').click(function() {
		$('button#answer').removeClass('hidden');
		$(this).parent().parent().addClass('hidden');
		$('input').val('');
	});
});