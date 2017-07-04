import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import "bootstrap/dist/css/bootstrap.css";
import { Navbar, NavItem, Nav, Grid, Row, Col } from "react-bootstrap";
const ALBUMS = [
  { name: "Orange channel", albumID: "623Ef2ZEB3Njklix4PC0Rs" },
  { name: "blond", albumID: "3mH6qwIy9crq0I9YQbOuDf" }
];

class AlbumDisplay extends Component {
  constructor() {
    super();
    this.state = {
      albumData: null
    };
  }
  componentDidMount() {
//curl -X "POST" -H "Authorization: Basic ZTU3NDI4MjQ3NDhiNDFlZTg4OTFkZTg4NjBiMjQwYWU6N2ZjOTg2ZTkzYjE4NDE0OGFiNDhmNzRlYzZiYTUwOTc=" -d grant_type=client_credentials https://accounts.spotify.com/api/token

//{"access_token":"BQDhc-_VgcJ_29Dg3989qGFlWWsRbPwBQtZEagjQkd_mkBnZ5sY0LRU9UVts3j7w3RO1jXe08fCSPlNaNeVLYA","token_type":"Bearer","expires_in":3600}
    const token = "Bearer BQDhc-_VgcJ_29Dg3989qGFlWWsRbPwBQtZEagjQkd_mkBnZ5sY0LRU9UVts3j7w3RO1jXe08fCSPlNaNeVLYA";
    const albumID = this.props.albumID;
    const albumURL = "https://api.spotify.com/v1/albums/" + albumID;
    const tracksURL = "https://api.spotify.com/v1/albums/" + albumID + "/tracks";
    fetch(albumURL, {
      method: "GET",
      headers: {
        "Accept": "application/json",
        "Authorization": token
      }
    }).then(res => res.json()).then(json => {
      this.setState({ albumData: json });
    });
    fetch(tracksURL, {
      method: "GET",
      headers: {
        "Accept": "application/json",
        "Authorization": token
      }
    }).then(res => res.json()).then(json => {
      this.setState({ songsData: json });
    });
  }
  render() {
    const songsData = this.state.songsData;
    const albumData = this.state.albumData;
    if (!albumData) return <div>Cargando...</div>;

    const title = albumData.name;

    const albumImg = albumData.images[0].url;

    var artists = albumData.artists[0].name;
    for (var i = 1; i < albumData.artists.length; i++) {
      artists += ", ";
      artists += albumData.artists[i].name;
    }

    var songs = [];
    for (var i = 0; i < songsData.items.length; i++) {
      songs.push(<li><a target="_blank" href={songsData.items[i].preview_url}>{songsData.items[i].name}</a></li>);
    }

    return (
      <div>
        <h3>{title}</h3>
        <h5>{artists}</h5>
        <hr/>
        <Row>
          <Col md={4} sm={4}>
            <img src={albumImg} width="100%" height="100%" className="album-cover" alt="Cover {title}"/>
          </Col>
          <Col md={4} sm={4}>
            <ol>
              {songs}
            </ol>
          </Col>
        </Row>
      </div>
    );
  }
}

class App extends Component {
  constructor() {
    super();
    this.state = {
      activeAlbum: 0
    };
  }
  render() {
    const activeAlbum = this.state.activeAlbum;
    return (
      <div>
        <Navbar>
          <Navbar.Header>
            <Navbar.Brand>Discos varios</Navbar.Brand>
          </Navbar.Header>
        </Navbar>
        <Grid>
          <Row>
            <Col md={3} sm={3}>
              <Nav
                bsStyle="pills"
                stacked
                activeKey={activeAlbum}
                onSelect={index => {
                  this.setState({ activeAlbum: index });
                }}
              >
                {ALBUMS.map((album, index) => (
                  <NavItem key={index} eventKey={index}>{album.name}</NavItem>
                ))}
              </Nav>
            </Col>
            <Col md={8} sm={8}>
              <AlbumDisplay key={activeAlbum} albumID={ALBUMS[activeAlbum].albumID} />
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default App;
