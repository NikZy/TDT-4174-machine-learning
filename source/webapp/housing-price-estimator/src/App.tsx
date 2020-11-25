import React from 'react';
import logo from './logo.svg';
import './App.css';
import { isVariableDeclaration } from 'typescript';
import { features as Features } from 'process';
import { maxHeaderSize } from 'http';

function App() {
  const predictedPriceTest = estimate_price(normalizeParameters(test));
  console.log(test);
  console.log(normalizeParameters(test));
  console.log(estimate_price(normalizeParameters(test)));
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
    center_distance: (variables.center_distance - -0.18773) / 0.094203,
    last_fixed: (variables.last_fixed - 0.029588) / 0.027193,
  };
};
const estimate_price = (variables: Features): number => {
  return (
    -1.20644943e4 * variables.bedrooms +
    1.68605256e4 * variables.bathrooms + // bathrooms
    6.00033306e4 * variables.sqft_living + // sqft_living
    2.28164262e4 * variables.sqft_lot + // sqft_lot
    1.96835599e4 * variables.floors + // floors
    1.31876732e-11 * variables.waterfront + //waterfont
    3.71400533e4 * variables.view + // view
    1.99840531e4 * variables.condition + //  condition
    9.86876017e4 * variables.grade + // grade
    4.84840553e4 * variables.sqft_above + // sqft_above
    3.38028639e4 * variables.sqft_basement + // sqft_basement code
    4.50330596e3 * variables.zip_code + //zip
    1.79925267e4 * variables.sqft_living15 + //  sqft_living15
    1.80663354e4 * variables.sqft_lot15 + // sqft_sqft_lot15
    9.19778574e4 * variables.center_distance + // center_distance
    6.00239138e4 * variables.last_fixed //  last_fixed
  );
};

export default App;
