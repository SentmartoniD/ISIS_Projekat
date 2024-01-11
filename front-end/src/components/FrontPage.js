import { useState } from "react";
import { SendUSHolidaysData, SendWeatherData, SendLoadData, TrainModel, BeginForecast, ShowGraph } from "../services/FrontPageService";

function FrontPage(){
    const [loadData, setLoadData] = useState([]);
    const [weatherData, setWeatherData] = useState([]);
    const [usHolidaysData, setUSHolidaysData] = useState();
    const [startDateForTraining, setStartDateForTraining] = useState();
    const [endDateForTraining, setEndDateForTraining] = useState();
    const [startDateForForecast, setStartDateForForecast] = useState();
    const [daysForForecast, setDaysForForecast] = useState();
    const [endDateForGraph, setEndDateForGraph] = useState();
    const [startDateForGraph, setStartDateForGraph] = useState();

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
        
        if(usHolidaysData === undefined && !weatherData.length && !loadData.length)
            return
        if(usHolidaysData === undefined)
            console.log("USHolidays data empty!")
        else if (hasExtension(usHolidaysData.name, ".xlsx"))
            try{
                const response = await SendUSHolidaysData(usHolidaysData);
                console.log(response);
            }catch(error){
                if (!error?.response)
                    alert("No server response!")
                else
                    alert(JSON.stringify(error.response.data))
            }
        else
            alert("The USHolidays file must be .xlsx!")
        
        if(!weatherData.length)
            console.log("Weather data empty!") 
        else if (hasExtension(weatherData[0].name, ".csv"))       
            try{
             const response = await SendWeatherData(weatherData);
             console.log(response);
            }catch(error){
                if (!error?.response)
                    alert("No server response!")
                else
                    alert(JSON.stringify(error.response.data))
            }
        else
            alert("The Weather files must be .csv!")

        if(!loadData.length)
            console.log("Load data empty!")
        else if (hasExtension(loadData[0].name, ".csv"))              
            try{
             const response = await SendLoadData(loadData);
             console.log(response);
            }catch(error){
                if (!error?.response)
                    alert("No server response!")
                else
                    alert(JSON.stringify(error.response.data))
            }
        else
            alert("The Load files must be .csv!")
      }

    const handleSubmitTrainModel = async (e) =>{
        if(startDateForTraining === undefined || endDateForTraining === undefined)
            alert("Pick both dates!")
        if(startDateForTraining > endDateForTraining)
            alert("The end date is before the start date, pick end date again!")
        try{
            const response = await TrainModel(startDateForTraining, endDateForTraining);
            console.log(response);
        }catch(error){
            if (!error?.response)
                alert("No server response!")
            else
                alert(JSON.stringify(error.response.data))
        }
      }

    const handleSubmitBeginForecast = async (e) =>{
        if(daysForForecast === undefined || startDateForForecast === undefined)
            alert("Pick a date and the number of days!")
        if(daysForForecast < 1 || daysForForecast > 7)
            alert("NUmber of days for forecast mus be bethween 1 and 7!")
        try{
            const response = await BeginForecast(startDateForForecast, daysForForecast);
            console.log(response);
        }catch(error){
            if (!error?.response)
                alert("No server response!")
            else
                alert(JSON.stringify(error.response.data))
        }        
      }

    const handleSubmitShowGraph = async (e) =>{
        if(startDateForGraph === undefined || endDateForGraph === undefined)
            alert("Pick both dates!")
        if(startDateForGraph > endDateForGraph)
            alert("The end date is before the start date, pick end date again!")
        try{
            const response = await ShowGraph(startDateForGraph, endDateForGraph);
            console.log(response);
        }catch(error){
            if (!error?.response)
                alert("No server response!")
            else
                alert(JSON.stringify(error.response.data))
        }
      }

    function hasExtension(fileName, ext){
        return fileName.toLowerCase().endsWith(ext.toLowerCase());
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
                    <input type="file" multiple directory="true" webkitdirectory="true" onChange={handleFilesChange2} ></input>
                </div>
                <div className="frontpage-div2">
                    <label className="frontpage-label" >US holidays data:</label>
                    <input type="file" onChange={handleFileChange} ></input>
                </div>
                <button className="frontpage-button" onClick={handleSubmitSendData} >SEND DATA</button>
                <label className="frontpage-label" >Start date for training</label>
                <input type="date" onChange={(e) => setStartDateForTraining(e.target.value)}></input>
                <label className="frontpage-label" >End date for training</label>
                <input type="date" onChange={(e) => setEndDateForTraining(e.target.value)}></input>
                <button className="frontpage-button" onClick={handleSubmitTrainModel} >TRAIN MODEL</button>
                <label className="frontpage-label" >Start date for forecast</label>
                <input type="date" onChange={(e) => setStartDateForForecast(e.target.value)} ></input>
                <label className="frontpage-label" >Number of days(max 7)</label>
                <input type="number" onChange={(e) => setDaysForForecast(e.target.value)} ></input>
                <button className="frontpage-button" onClick={handleSubmitBeginForecast} >BEGIN FORECAST</button>
                <label className="frontpage-label" >Start date for graph</label>
                <input type="date" onChange={(e) => setStartDateForGraph(e.target.value)} ></input>
                <label className="frontpage-label" >End date for graph</label>
                <input type="date" onChange={(e) => setEndDateForGraph(e.target.value)} ></input>
                <button className="frontpage-button" onClick={handleSubmitShowGraph} >SHOW GRAPH</button>
            </div>
        </section>
    )
}




export default FrontPage;