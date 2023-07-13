var jwt = require('jsonwebtoken');

function issueToken(payload) {
    const secretKey = process.env.JWT_SECRET_KEY;
    const token = jwt.sign(payload, secretKey);
    return token;
}

function verifyToken(token) {
    const secretKey = process.env.JWT_SECRET_KEY;
    try {
        const decoded = jwt.verify(token, secretKey);
        return decoded;
      } catch(err) {
        return undefined;
      }
}


module.exports = {
    issueToken,
    verifyToken
}
