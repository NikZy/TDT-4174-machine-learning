import React from 'react';
import logo from './logo.svg';
import './App.css';
import { isVariableDeclaration } from 'typescript';
import { features as Features } from 'process';
import { maxHeaderSize } from 'http';
import { Controller, useForm } from 'react-hook-form';
import { Slider } from '@material-ui/core';
import { FormControl } from '@material-ui/core';

const ApiPost = (url, data) =>
  fetch(`http://localhost:5000/` + url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  }).then((res) => res.json());
function App() {
  const { register, handleSubmit, watch, errors, control } = useForm();
  const predictedPriceTest = estimate_price(normalizeParameters(test));
  const onSubmit = (data) => {
    console.log('Data:');
    console.log(data);
    const dataConvertedToInts = convertIntObj(data);
    console.log(convertIntObj(data));
    const features = Object.assign(test, dataConvertedToInts);
    console.log(features);
    ApiPost('estimator', features)
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  };
  console.log(test);
  // console.log(normalizeParameters(test));
  // console.log(estimate_price(normalizeParameters(test)));
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input
          type="number"
          name="bedrooms"
          defaultValue="2"
          // ref={register({ required: true })}
        />
        Grade
        <Controller
          name="grade"
          defaultValue={7}
          as={<Slider min={0} max={10} valueLabelDisplay="on" step={1} />}
          control={control}
        />
        <Slider
          min={0}
          valueLabelFormat="bedroom"
          name="bathrooms"
          defaultValue={7}
          max={10}
          innerRef={register}
          // ref={register}
          valueLabelDisplay="on"
          step={1}
        />
        {errors.bedroom && <span>This field is required</span>}
        <input type="submit" />
      </form>
      <h1>
        {predictedPriceTest ? estimate_price(normalizeParameters(test)) : 0}
      </h1>
    </div>
  );
}
const calculateCenterDistance = (lat: number, long: number): number => {
  const latCenter = 47.63;
  const longCenter = -122.2;
  return (lat - latCenter) ** 2 + (long - longCenter) ** 2;
};

const calculateLastFixed = (built: number, renovate: number) => {
  // hva gjøres her?
  /*     lastFixedList[i] = (2020 - max(df.at[i, 'yr_built'],
                                   df.at[i, 'yr_renovated'])) / df.at[i, 'sqft_living'] */
  return 2020 - Math.max(built, renovate);
};

function convertIntObj(obj) {
  const res = {};
  for (const key in obj) {
    const parsed = parseInt(obj[key]);
    res[key] = parsed;
    res[key] = isNaN(parsed) ? obj[key] : parsed;
  }
  return res;
}
interface Features {
  bathrooms: number;
  bedrooms: number;
  sqft_living: number;
  sqft_lot: number;
  waterfront: number;
  floors: number;
  view: number;
  condition: number;
  grade: number;
  sqft_above: number;
  sqft_basement: number;
  zip_code: number;
  sqft_living15: number;
  sqft_lot15: number;
  center_distance: number;
  last_fixed: number;
}

const test: Features = {
  bathrooms: 1,
  bedrooms: 3,
  sqft_living: 1180,
  sqft_lot: 5650,
  floors: 1,
  waterfront: 0,
  view: 0,
  condition: 3,
  grade: 7,
  sqft_above: 1180,
  sqft_basement: 0,
  last_fixed: calculateLastFixed(1955, 0),
  zip_code: 98178,
  sqft_living15: 1340,
  sqft_lot15: 5650,
  center_distance: calculateCenterDistance(47.5112, -122.257),
};
/* const test2: Features = {
  bedrooms: 2,
  bathrooms: -0.3987371485515761,
  sqft_living:-1.4474635685648216,
  sqft_lot: -0.9036171393191288,
  floors: -0.1287548306162246,
  waterfront: -0.9154270041565511,
  view: -0.08717263102067989,
  condition: -0.30575946383494007,
  grade: 0.9075535361389149,
  sqft_above: -0.5588357490736213,
  -0.6501739072174175,-0.6586810403679764,-1.400644831402753,-1.0308984565214254,-0.14351452261811226,-1.3417547735375033,0.41231859187110054 */
const normalizeParameters = (variables: Features): Features => {
  // subracting the average
  // dividing by standard deviation
  return {
    bedrooms: (variables.bedrooms - 3.370842) / 0.930062,
    bathrooms: (variables.bathrooms - 2.114757) / 0.770163,
    sqft_living: (variables.sqft_living - 2079.9) / 918.44089,
    sqft_lot: (variables.sqft_lot - 15106.97) / 41420.5,
    floors: (variables.floors - 1.494309) / 0.539989,
    waterfront: (variables.waterfront - 0.007542) / 0.086517,
    view: (variables.view - 0.234303) / 0.766318,
    condition: (variables.condition - 3.40943) / 0.650743,
    grade: (variables.grade - 7.656873) / 1.175459,
    sqft_above: (variables.sqft_above - 1788.39) / 828.1,
    sqft_basement: (variables.sqft_basement - 291.51) / 442.575043,
    zip_code: (variables.zip_code - 98077.94) / 53.51,
    sqft_living15: (variables.sqft_living15 - 1986.55) / 685.4,
    sqft_lot15: (variables.sqft_lot15 - 12768.45) / 27304.18,
    center_distance: (variables.center_distance - 0.18773) / 0.094203,
    last_fixed: (variables.last_fixed - 0.029588) / 0.027193,
  };
};
const estimate_price = (variables: Features): number => {
  return (
    -12064.4943 * variables.bedrooms +
    16860.5256 * variables.bathrooms + // bathrooms
    60003.3306 * variables.sqft_living + // sqft_living
    22816.4262 * variables.sqft_lot + // sqft_lot
    19683.5599 * variables.floors + // floors
    53372.09013601506 * variables.waterfront + //waterfont
    37140.0533 * variables.view + // view
    19984.0531 * variables.condition + //  condition
    98687.6017 * variables.grade + // grade
    48484.0553 * variables.sqft_above + // sqft_above
    33802.8639 * variables.sqft_basement + // sqft_basement code
    4503.30596 * variables.zip_code + //zip
    17992.5267 * variables.sqft_living15 + //  sqft_living15
    -18066.3354 * variables.sqft_lot15 + // sqft_sqft_lot15
    91977.8574 * variables.center_distance + // center_distance
    60023.9138 * variables.last_fixed + //  last_fixed
    524327 * 1
  );
};

export default App;
