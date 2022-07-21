import { Component } from '@angular/core';

type Movie = {
  name: String,
  available: number,
  quantity: number,
};
type Movies = Array<Movie>;

@Component({
  selector: 'app-root',
  // template: `<h2>Hey!</h2>`
  templateUrl: './app.component.html',
  // styleUrls: ['./app.component.css']
})
export class AppComponent {
  title: String = 'Movies';
  movies: Movies = [
  {
      name: "Avengers",
      available: 5,
      quantity: 0,
  },
  {
    name: "Forest Gump",
    available: 2,
    quantity: 0,
  },
  ];

  addMovieQuantity (movieName: String){
    const movieIndex: number = this.movies.findIndex(
      movie => movie.name === movieName,
    );

      this.movies[movieIndex].quantity += 1;
  }

  rmvMovieQuantity (movieName: String){
    const movieIndex: number = this.movies.findIndex(
      movie => movie.name === movieName,
    );

      this.movies[movieIndex].quantity -= 1;
  }
}
