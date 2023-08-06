# This file contains all implementation of the Nitrogen Estimation Methods that were used in literature

from turtle import shape
import numpy as np

def M1(img):
    """
        R: average red component.
    """
    return np.nanmean(img[:,:,0])


def M2(img):
    """
        G: average green component.
    """

    return np.nanmean(img[:,:,1]) 


def M3(img):
    """
        B: average blue component.
    """

    return np.nanmean(img[:,:,2])


def M4(img):
    """
        R / (R + G + B)
    """

    return np.nanmean(img[:,:,0] / (img[:,:,0].astype(int) + img[:,:,1] + img[:,:,2]))

def M5(img):
    """
        G / (R + G + B)
    """

    return np.nanmean(img[:,:,1] / (img[:,:,0].astype(int) + img[:,:,1] + img[:,:,2]))


def M6(img):
    """
        B / (R + G + B)
    """

    return np.nanmean(img[:,:,2] / (img[:,:,0].astype(int) + img[:,:,1] + img[:,:,2]))


def M7(img):
    """
        R - G
    """
    
    return np.nanmean(abs(img[:,:,0].astype(int) - img[:,:,1]))


def M8(img):
    """
        R - B
    """

    return np.nanmean(abs(img[:,:,0].astype(int) - img[:,:,2]))


def M9(img):
    """
        G - B
    """

    return np.nanmean(abs(img[:,:,1].astype(int) - img[:,:,2]))


def M10(img):
    """
        (R - G) / (R + G)
    """

    return np.nanmean(abs(img[:,:,0].astype(int) - img[:,:,1]) / (img[:,:,0].astype(int) + img[:,:,1]))


def M11(img):
    """
        (R - B) / (R + B)
    """

    return np.nanmean(abs(img[:,:,0].astype(int) - img[:,:,2]) / (img[:,:,0].astype(int) + img[:,:,2]))

def M12(img):
    """
        (G - B) / (G + B)
    """

    return np.nanmean(abs(img[:,:,1].astype(int) - img[:,:,2]) / (img[:,:,1].astype(int) + img[:,:,2]))


def M13(img):
    """
        (R - G) /(R + G + B)
    """

    return np.nanmean(abs(img[:,:,0].astype(int) - img[:,:,1]) / (img[:,:,0].astype(int) + img[:,:,1] + img[:,:,2]))


def M14(img):
    """
        (R - B) /(R + G + B)
    """

    return np.nanmean(abs(img[:,:,0].astype(int) - img[:,:,2]) / (img[:,:,0].astype(int) + img[:,:,1] + img[:,:,2]))


def M15(img):
    """
        (G - B) /(R + G + B)
    """

    return np.nanmean(abs(img[:,:,1].astype(int) - img[:,:,2]) / (img[:,:,0].astype(int) + img[:,:,1] + img[:,:,2]))


def M16(img):
    """
        (2 * R * (G - B)) / (G + B)
    """

    return np.nanmean((2*img[:,:,0]*abs(img[:,:,1].astype(int) - img[:,:,2])) / (img[:,:,1].astype(int) + img[:,:,2]))


def M17(img):
    """
        (2 * G * (R - B)) / (R + B)
    """

    return np.nanmean((2*img[:,:,1]*abs(img[:,:,0].astype(int) - img[:,:,2])) / (img[:,:,0].astype(int) + img[:,:,2]))

