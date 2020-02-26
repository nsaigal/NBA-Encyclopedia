import React from 'react';
import '../App.css';

class PlayerCard extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (

            <div className='player-card'>
                <img class='player-image' alt={this.props.player_name} src='https://nomadlist.com/assets/img/cities/barcelona-spain-600px.jpg'></img>
                <div className='dimmer'></div>
                <div className='player-text'>
                    <h2 className='player-name'>
                        {this.props.player_name}
                    </h2>
                    <h3 className='player-active-years'>
                        {this.props.active_years}
                    </h3>
                </div>

            </div>
        );
    }
}

export default PlayerCard;
