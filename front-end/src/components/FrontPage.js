import { useState } from "react";
import { SendUSHolidaysData, SendWeatherData, SendLoadData } from "../services/FrontPageService";

function FrontPage(){
    const [loadData, setLoadData] = useState([]);
    const [weatherData, setWeatherData] = useState([]);
    const [usHolidaysData, setUSHolidaysData] = useState();
    const [dateRange, setDateRange] = useState();

    const handleFilesChange1 = (event) => {
        const files = event.target.files;
        const filesArray = Array.from(files);
        setLoadData(filesArray);
      };

    const handleFilesChange2 = (event) => {
        const files = event.target.files;
        const filesArray = Array.from(files);
        setWeatherData(filesArray);
      };

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        setUSHolidaysData(selectedFile);
      };

    const handleSubmitSendData = async (e) =>{
        try{
            const response = await SendUSHolidaysData(usHolidaysData);
            console.log(response);
        }catch(error){
            if (!error?.response)
                alert("No server response!")
            else
                alert(JSON.stringify(error.response.data))
        }
        try{
            const response = await SendWeatherData(weatherData);
            console.log(response);
        }catch(error){
            if (!error?.respons)
                alert("No server response!")
            else
                alert(JSON.stringify(error.response.data))
        }
        try{
            const response = await SendLoadData(loadData);
            console.log(response);
        }catch(error){
            if (!error?.respons)
                alert("No server response!")
            else
                alert(JSON.stringify(error.response.data))
        }
      }

    const handleSubmitTrainModel = async (e) =>{
 
      }

    const handleSubmitBeginForecast = async (e) =>{

      }

    return(
        <section className="frontpage-section" >
            <h1 className="frontpage-h1" >Electricity consumption forecast</h1>
            <div className="frontpage-div-control" > 
                <div className="frontpage-div2" >
                    <label className="frontpage-label" >Load data:</label>
                    <input type="file" multiple directory="true" webkitdirectory="true" onChange={handleFilesChange1} ></input>
                </div>
                <div className="frontpage-div2">
                    <label className="frontpage-label" >Weather data:</label>
                    <input type="file" multiple onChange={handleFilesChange2} ></input>
                </div>
                <div className="frontpage-div2">
                    <label className="frontpage-label" >US holidays data:</label>
                    <input type="file" onChange={handleFileChange} ></input>
                </div>
                <button className="frontpage-button" onClick={handleSubmitSendData} >SEND DATA</button>
                <label>Start date for forecast</label>
                <input type="date" ></input>
                <label>End date for forecast</label>
                <input type="date" ></input>
                <button className="frontpage-button" onClick={handleSubmitTrainModel} >TRAIN MODEL</button>
                <label>Starting date</label>
                <input type="date" ></input>
                <label>Number of days(max 7)</label>
                <input type="number" ></input>
                <button className="frontpage-button" onClick={handleSubmitBeginForecast} >BEGIN FORECAST</button>
                <button className="frontpage-button" onClick={handleSubmitBeginForecast} >SHOW GRAPH</button>
            </div>
        </section>
    )
}




export default FrontPage;