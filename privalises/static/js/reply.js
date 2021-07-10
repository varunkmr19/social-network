function commentReplyToggle(parent_id)
{
	const row = document.getElementById(parent_id);
	if (row.classList.contains('d-none'))
	{
		row.classList.remove('d-none');
	}
	else
	{
		row.classList.add('d-none')
	}

}

/*function formatTags() {
	const elements = document.getElementsByClassName('tags-id');
	for (let i = 0; i < elements.length; i++) {
		let bodyText = elements[i].children[0].innerText;

		let words = bodyText.split(' ');

		for (let j = 0; j < words.length; j++) {
			if (words[j][0] === '#') {
				let replacedText = bodyText.replace(/\s\#(.*?)(\s|$)/g, ` <a href="#">${words[j]}</a>`);
				elements[i].innerHTML = replacedText;
				console.log(words[j].slice(1))
			}
		}
	}
}
function formatMentions() {
	const elements = document.getElementsByClassName('mentions-id');
	for (let i = 0; i < elements.length; i++) {
		let bodyText = elements[i].children[0].innerText;

		let words = bodyText.split(' ');

		for (let j = 0; j < words.length; j++) {
			if (words[j][0] === '@') {
				let replacedText = bodyText.replace(/(^|\s)\@(.*?)(\s|$)/g, ` <a href="/profile/${words[j].slice(1)}">${words[j]}</a> `);
				elements[i].innerHTML = replacedText;
				console.log(words[j].slice(1))
			}
		}
	}
}*/

function formatTags() {
	const elements = document.getElementsByClassName('tags-id');
	for (let i = 0; i < elements.length; i++) {
		let bodyText = elements[i].children[0].innerText;

		let words = bodyText.split(' ');

		replacedText = ""
		for (let j = 0; j < words.length; j++) {
			if (words[j][0] === '#') {
				words[j] = `<a href="#">${words[j]}</a>`
			}
			if (words[j][0] === '@') {
				words[j] = `<a href="/profile/${words[j].slice(1)}">${words[j]}</a>`
			}
		}
		elements[i].innerHTML = words.join(' ');
	}
}

formatTags();