import React from 'react';
import './App.css';
import FilterButton from './components/FilterButton.js';
import FilterTray from './components/FilterTray.js';
import PlayerCard from './components/PlayerCard';
import Slider from './components/Slider.js';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      players:[],
      showFilters: false,
      filterButtonText: 'Show Filters',
      mainClass:'main',
      filterClass:'filter-tray',
      ageParams: ['18', '70'],
      heightParams: ['65', '92'],
      weightParams: ['150', '380'],
      activeYearsParams: ['1950', '2019']
    };
    this.filterButtonClick = this.filterButtonClick.bind(this);
  }

  componentDidMount() {
    this.getPlayers();
  }

  getPlayers() {
    var queryStringAY = '?start_year=' + this.state.activeYearsParams[0] + '&end_year=' + this.state.activeYearsParams[1]
    var queryStringHeight = '&from_height=' + this.state.heightParams[0] + '&to_height=' + this.state.heightParams[1]
    var queryStringWeight = '&from_weight=' + this.state.weightParams[0] + '&to_weight=' + this.state.weightParams[1]
    var queryStringAge = '&from_age=' + this.state.ageParams[0] + '&to_age=' + this.state.ageParams[1]

    fetch('http://localhost:3000/api/players' + queryStringAY + queryStringHeight + queryStringWeight + queryStringAge)
    .then(res => res.json())
    .then((data) => {
      this.setState({ players: data })
    })
    .catch(console.log)
  }

  filterButtonClick() {
    this.setState({
      showFilters: !this.state.showFilters
    });
    
    var newValue = '';
    newValue = (this.state.filterButtonText === 'Show Filters')
        ? 'Hide Filters'
        : 'Show Filters'

    this.setState({
      filterButtonText: newValue
    })

    var newClasses = (this.state.showFilters) ? 'main slideOut': 'main slideIn'
    this.setState({
      mainClass: newClasses
    })

    var newClasses = (this.state.showFilters) ? 'filter-tray hideTray': 'filter-tray showTray'
    this.setState({
      filterClass: newClasses
    })
  }

  ActiveYearsSliderChange = (value) => {
    this.setState({activeYearsParams: [value, '2019']});
    this.getPlayers();
  }

  HeightSliderChange = (value) => {
    this.setState({heightParams: [value, '92']});
    this.getPlayers();

  }

  WeightSliderChange = (value) => {
    this.setState({weightParams: [value, '350']});
    this.getPlayers();

  }

  AgeSliderChange = (value) => {
    this.setState({ageParams: [value, '70']});
    this.getPlayers();

  }
    
  render() {
    var players = this.state.players;
    return (
      <div className='container'>
        <div className={this.state.mainClass}>
          <h1 className='header'>
            NBA Player Finder
          </h1>
          <FilterButton filtersText={this.state.filterButtonText} onButtonClick={this.filterButtonClick}/>
          <div className='player-grid-container'>
            {players.map(value =>
              <div className='player-grid-list-item'>
                <PlayerCard player_name={value.first_name + ' ' + value.last_name}  active_years={value.start_year + ' - ' + value.end_year}/>
              </div>
              )}
          </div>
        </div>
        <FilterTray class={this.state.filterClass} ActiveYearsSliderChange={this.ActiveYearsSliderChange} HeightSliderChange={this.HeightSliderChange} WeightSliderChange={this.WeightSliderChange} AgeSliderChange={this.AgeSliderChange}></FilterTray>
      </div>
    );
  }
}

export default App;
