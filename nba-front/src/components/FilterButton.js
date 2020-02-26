import React from 'react';
import '../App.css';

class FilterButton extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <button className='filter-button' onClick={this.props.onButtonClick}>
                {this.props.filtersText}
            </button>
        );
    }
}

export default FilterButton;
