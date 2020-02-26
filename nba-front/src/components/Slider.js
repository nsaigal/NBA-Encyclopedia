import React from 'react';
import '../App.css';

class Slider extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className='slider-container'>
                <input id={'slider-' + this.props.id} onChange={this.props.slideChange} type='range' min={this.props.min} max={this.props.max} className='slider' style={{background:this.props.color}}></input>
            </div>
        );
    }
}

export default Slider;
