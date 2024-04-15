import React from 'react';

const Board = ({ id, title, contents, created_date }) => {
    return (
        <div>
            <h2>{title}</h2>
            <h5>{created_date}</h5>
            <hr />
            <p>{contents}</p>
        </div>
    );
};

export default Board;