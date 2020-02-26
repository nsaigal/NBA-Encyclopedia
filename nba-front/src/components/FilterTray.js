import React from 'react';
import '../App.css';
import Slider from '../components/Slider'

class FilterTray extends React.Component {
    constructor(props) {
        super(props);
        this.state = this.props.state;
    }

    AYSliderChange = () => {
        var input = document.getElementById("slider-1");
        var currentVal = input.value;
        this.props.ActiveYearsSliderChange(currentVal);
    }

    HeightSliderChange = () => {
        var input = document.getElementById("slider-2");
        var currentVal = input.value;
        this.props.HeightSliderChange(currentVal);
    }

    WeightSliderChange = () => {
        var input = document.getElementById("slider-3");
        var currentVal = input.value;
        this.props.WeightSliderChange(currentVal);
    }

    AgeSliderChange = () => {
        var input = document.getElementById("slider-4");
        var currentVal = input.value;
        this.props.AgeSliderChange(currentVal);
    }

    render() {
        return (
            <div className={this.props.class}>
                <h2 className='subheader'>FILTERS</h2>
                
                <h3 className='filter-label'>ACTIVE YEARS</h3>
                <Slider id='1' color='#4FD99F' min='1950' max='2019' slideChange={this.AYSliderChange}/>

                <h3 className='filter-label'>HEIGHT</h3>
                <Slider id='2' color='#F3A024' min='65' max='92' slideChange={this.HeightSliderChange}/>

                <h3 className='filter-label'>WEIGHT</h3>
                <Slider id='3' color='#4A65F1' min='150' max='380' slideChange={this.WeightSliderChange}/>

                <h3 className='filter-label'>AGE</h3>
                <Slider id='4' color='#D94F57' min='18' max='70' slideChange={this.AgeSliderChange}/>
            </div>
        );
    }
}

export default FilterTray;
