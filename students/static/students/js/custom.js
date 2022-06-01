function showPreview(event){
	if (event.target.files.length > 0) {
		let scr = URL.createObjectURL(event.target.files[0]);
		let preview = document.getElementById('file-preview');
		preview.scr = scr;
		preview.style.display = 'block';
	}
}