import axios from "axios"

export const Pelda = async () => {
    return await axios.get(`${process.env.REACT_APP_PYTHON_APP_API_URL}/`);
}