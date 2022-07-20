import logo from './logo.svg';
import form from './form'
import Form from './form';

const movies = [
  {
    name: 'Avengers',
    available: 5,
  },
  {
    name: "Forest Gump",
    available: 6
  }
];


function App() {
  return (
    <div className="App-header">
      <header> <h2>Movies</h2> </header>

      {movies.map( movie => (

        <Form movie={movie}/>

      ))}

    </div>

  );
}

export default App;
