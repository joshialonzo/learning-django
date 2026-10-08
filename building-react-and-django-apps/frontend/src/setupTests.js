import '@testing-library/jest-dom';
import { TextEncoder, TextDecoder } from 'util';

// React Router 7 needs these, and the jsdom environment in react-scripts 5 lacks them.
Object.assign(global, { TextEncoder, TextDecoder });
