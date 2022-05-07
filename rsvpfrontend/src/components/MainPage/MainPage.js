import './MainPage.css';
import { useState, useContext, useEffect } from "react";
import Form from 'react-bootstrap/Form';
import { useParams } from "react-router";

function MainPage() {
    const [numb, setNumb] = useState(0);
    let { id } = useParams();

    return (
        <>
            <input
                type="number"
                step="any"
                min="0"
                max="1"
                value={numb}
                onChange={(e) => setNumb(e.target.value)}
            />
        </>
    )
}

export default MainPage;