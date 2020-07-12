const sequelize = require('../util/db');
const { DataTypes } = require('sequelize');

const Chat = sequelize.define('Chat', {
    id: {
        type: DataTypes.UUID,
        defaultValue: DataTypes.UUIDV4,
        allowNull: false,
        primaryKey: true,
    },
    userOne: {
        type: DataTypes.STRING,
        allowNull: false,
        default: '',
    },
    userTwo: {
        type: DataTypes.STRING,
        allowNull: false,
        default: '',
    },
    isDeleted: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        default: false,
    },
    name: {
        type: DataTypes.STRING,
        allowNull: false,
        default: '',
    },
});

module.exports = Chat