export default class Process {
  constructor(socket, terminal, container_details) {
    this.socket = socket;
    this.terminal = terminal;
    this.pstatus = false;
    this.container = container_details.container;
    this.dir = container_details.dir;
  }

  sendCommand(command) {}
}
