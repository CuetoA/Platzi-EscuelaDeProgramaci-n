var articles = [
    {nameo: "bicycle", cost: 3000},
    {nameo: "car", cost: 50000},
    {nameo: "subway", cost: 5},
    {nameo: "phone", cost: 4000},
    {nameo: "belt", cost: 200},
    {nameo: "kindle", cost: 1700},
    {nameo: "speaker", cost: 3000}
]

var cheap_articles = articles.filter(function(article){
    return article.cost <= 10
});  // filter articles by price

var article_name = articles.map(function(article){
    return article.nameo
});  // returns what you want for the array in an array

var car = articles.find(function(article){
    return article.nameo === "car"
}); // find and return the first element that meet the condition

articles.forEach(function(article){
    console.log(article.nameo);
}); // does what the functions says for each element in the array

var cheap_articles = articles.some(function(article){
    return article.cost <= 700;
}) // return true or false if any element meet the condition