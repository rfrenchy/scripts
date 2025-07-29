import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className='character-menu' style={{ 'background-color': 'blue' }}>
        <Character name="Cloud" lv="48" hp="3000/3000" mp="264/473"/>
        <Character name="Tifa" lv="44" hp="3200/3200" mp="118/393"/>
        <Character name="Barret" status="Sadness" lv="45" hp="3334/3334" mp="212/361"/>
      </div>
      <div className='selection-menu'></div>
    </div>
  );
}

function Character({name, lv, status, hp, mp}) {
  return (
    <div className='character-inner'>
      <img className="character-image" src='.'></img>
      <div className='character-stats'>
        <span className='character-stat'><span>{name}</span><span>{status}</span></span>
        <span className='character-stat'><span>LV</span><span>{lv}</span></span>
        <span className='character-stat'><span>HP</span><span>{hp}</span></span>
        <span className='character-stat'><span>MP</span><span>{mp}</span></span>
      </div>
      <div className='limit-break-menu'>
        <span>next level</span>
        <svg></svg>
        <span>Limit level 2</span>
        <svg></svg>
      </div>
    </div>
  )
}

export default App;
