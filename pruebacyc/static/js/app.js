const apiKey = '93b3195a65fd4e88bdfd600565309e65';
const main = document.querySelector('main');

Window.addEventListener('load', e => {
	updateNews();
});

async function updateNews() {
	const res = await fetch('https://newsapi.org/v2/everything?q=bitcoin&from=2018-11-12&sortBy=publishedAt&apiKey=API_KEY')
	const json = await res.json():

	main.innerHTML = json.articles.map(createArticle).join('/n');
}

function createArticle(article){
	return `
	    <div class="article">
	      <a href="${article.url}">
	        <h2>${article.title}</h2>
	      </a>
	    </div>
	    `;
}

